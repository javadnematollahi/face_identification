from setuptools import setup,find_packages


def pre_install():
    f = open("readme.md", "r")
    text = f.read()
    return text

def requires():
    f = open("requirements.txt", "r")
    text = f.read()
    text = text.strip("\n").split("\n")
    return text

setup(
    name= "face_identification",
    version= "1.0.0",
    author="javad nematollahi",
    description="This app is a face identifier. If your face is existed in face bank, you recieved True, otherwise False.",
    long_description=pre_install(),
    install_requires=requires(),
    entry_points={
        'console_scripts': [
            'fi = face_identification:main',
        ],
    },
    author_email="javadnematollahi92@gmail.com",
    packages=find_packages()
)


