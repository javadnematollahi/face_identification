import cv2
from insightface.app import FaceAnalysis
import numpy as np
import argparse
from creat_face_bank import AddUser
import time


class FaceIdentification:
    def __init__(self, threshold=25) :
        self.app = FaceAnalysis(providers=['CPUExecutionProvider'], name='buffalo_s')
        self.app.prepare(ctx_id=0, det_size=(640, 640))
        self.threshold = threshold
        self.facebank = AddUser(self.app, self.threshold)
        # self.url='http://192.168.112.69:8080/video'

    def update(self, npy_face_bank_path:str="face_bank.npy", url:str =""):
        self.facebank.update_face_bank(npy_face_bank_path, url)

    def face_identification(self, npy_face_bank_path:str="face_bank.npy", url:str =""):
        try:
            face_bank = np.load(npy_face_bank_path, allow_pickle=True)
        except:
            np.save(npy_face_bank_path, [])
            face_bank = np.load(npy_face_bank_path, allow_pickle=True)
        print("len", len(face_bank))
        access = False
        no_camera = False

        if url == "":
            video = cv2.VideoCapture(0)
        else:
            video = cv2.VideoCapture(url)
        _,frame = video.read()
        if isinstance(frame, np.ndarray):
            no_camera = False
        elif isinstance(frame, type(None)):
            no_camera = True

        if no_camera == False:
            video.set(3,1280)
            video.set(4,960)
            start_time = time.time()
            while (time.time()-start_time<5):
                ok,frame = video.read()

                if not ok:
                    break
                image_g = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                resultg = self.app.get(image_g)
                if len(resultg) == 1:
                    for result in resultg:
                        for person in face_bank:
                            face_bank_person_embedding = person["embedding"]
                            new_person_embedding = result["embedding"]
                            distance = np.sqrt(np.sum((face_bank_person_embedding - new_person_embedding)**2))
                            if distance < self.threshold:
                                access = True
                                print("Access ok")
                                break
                        else:
                            access = False
                            print("Access denied")
                        break
                    break
            return access
        else:
            return "No Camera"



parser = argparse.ArgumentParser()
parser.add_argument('--update',default=True, action='store_true', help='Update face_bank')
parser.add_argument('--npyfile', default="face_bank.npy", help='Npy face_bank file path')
parser.add_argument('--url', default="", help='Npy face_bank file path')
opt = parser.parse_args()
fi = FaceIdentification()

def main(npy_file_path:str=opt.npyfile, url:str=opt.url, update=False):
    if update:
        fi.update(npy_file_path, url)
    result = fi.face_identification(npy_file_path, url)
    return result

if __name__ == "__main__":
    main()