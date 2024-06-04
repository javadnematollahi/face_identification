## Face Identifier

Feature of this app:

You can created a new facebank and add your face as a new face.
You can add as many face as you want to the facebank.
If a face exist in your face bank, app detect that face and return True.
If a face doesn't exist in facebank, app return False.

# how to use:

you can use this app in two way:
in Command Line Interface(CLI) or in your Python environment.

In CLI use below command:

```
fi --url http://192.168.112.69:8080/video --update
```
If you use ```--update``` app first will try to add a new face face to facebank, so if you want to do this, be sure to put yur face in front of camera.

If you set url as ```--url http://192.168.112.69:8080/video``` app will use it to connect to a camera. If your system has a webcam or camera you can leave this parameter empty, so app automatically connect to first finded camera.

You can use ```npy_file_path="new_facebank.npy"``` if you want to create a new facebank

In Python environment:

```
import face_identification as fi
fi = fi()
result = face_identification.main(url='url of your camera')  ->url of your camera, if your system has a camera leave it as an empty string (example url ="http://192.168.112.69:8080/video")

# set update=True if you want add new face to facebank
result = face_identification.main(url='url of your camera', update=True)

# set npy_file_path="new_facebank.npy" if you want to create a new facebank:
result = face_identification.main(url='url of your camera', , npy_file_path="new_bank.npy")

result would be True if your face was added to facebank.
result would be False if your face hadn't been added to facebank.
```

# How to install 

```
pip install face_identidfy
```