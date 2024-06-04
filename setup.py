from setuptools import setup


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
    long_description_content_type='text/markdown',
    install_requires=requires(),
    entry_points={
        'console_scripts': [
            'fi = face_identification:main',
        ],
    },
    author_email="javadnematollahi92@gmail.com",
    packages=['face_identification']
)


