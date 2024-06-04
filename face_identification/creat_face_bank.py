import cv2
import numpy as np
import time

class AddUser:
    def __init__(self, app, threshold):
        self.app = app
        self.threshold = threshold
        # self.url='http://192.168.229.162:8080/video'

    def creat_face_bank(self, update:bool=False, url:str="", npy_path=""):
        face_bank = []
        recognize = 0 
        no_camera = False
        try:
            if url == "":
                video = cv2.VideoCapture(0)
            else:
                video = cv2.VideoCapture(url)
        except:
            no_camera = True
        if no_camera == False:
            _,frame = video.read()
            if isinstance(frame, np.ndarray):
                print(type(frame))
            elif isinstance(frame, type(None)):
                return True

            video.set(3,1280)
            video.set(4,960)
            face_ok = False
            start = time.time()
            while True:
                ok,frame = video.read()

                if not ok:
                    break
                result = self.app.get(frame)
                if len(result) > 1:
                    print("warning: more than one face detected in image")
                    continue
                if len(result)==1:
                    face_ok = True
                    embedding = result[0]['embedding']
                    my_dict = {"embedding": embedding}
                    face_bank.append(my_dict)
                    break
                finish = time.time()
                if finish - start>10:
                    recognize = 1
                    break
            if update == False and face_ok == True:
                print(f"Your face is set as Login Face.")
                np.save(npy_path, face_bank)
            elif recognize == 1:
                print(f"Next time put your face in front of camera. ")
                return False
            else:
                return face_bank
        else:
            return True

    def update_face_bank(self, last_npy_facebank_path, url: str=""):
        try:
            facebank = np.load(last_npy_facebank_path , allow_pickle=True)
        except:
            np.save(last_npy_facebank_path, [])
            facebank = np.load(last_npy_facebank_path , allow_pickle=True)
        newfacebank = self.creat_face_bank(update=True, url=url, npy_path=last_npy_facebank_path)
        if isinstance(newfacebank, list):
            for result in newfacebank:
                for person in facebank:
                    face_bank_person_embedding = person["embedding"]
                    new_person_embedding = result["embedding"]
                    distance = np.sqrt(np.sum((face_bank_person_embedding - new_person_embedding)**2))
                    if distance < self.threshold:
                        print("Your face is already existed in facebank.")
                        break
                else:
                    facebank = np.append(facebank,np.array([{"embedding": newfacebank[0]['embedding']}]))
                    np.save(last_npy_facebank_path, facebank)
                    print(len(facebank))
                    print("Your face is added to login users.")
        elif newfacebank == True:
            print("No camera detected")
        elif newfacebank == False:
            print("There is no face in the camera.")

if __name__ == "__main__":
    create = AddUser()
    create.creat_face_bank( url="", npy_path="face_bank.npy")


