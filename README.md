# deepface_face_verification

#This is a face verification project used to check the two images passed to the programme are of the same person or not, using Deepface framework. Deepface is a hybrid face recognition framework which wraps most of the well known models, which are VGG-Face, Google FaceNet, OpenFace, Facebook DeepFace, DeepID, ArcFace, Dlib and SFace. While executing face_verification.py, we could pass our desired model we want to use or we can pass multiple models, so that we can compare the performance of each model.


#Steps to execute the code:

#cd into the deepface_face_verification directory and create a venv virtual environment and activate it by:

#python -m venv <virtual environment name>
#source <virtual environment name>/bin/activate

#Then to install the required packages do:

#pip install -r requirements.txt

#To run the face_verification.py in the terminal do the following:

#python face_verification.py <path to first image> <path to second image> <model> <model> ..... <model>

#e.g. python face_verification.py /home/arpan/face/test1.jpg /home/arpan/face/test2.jpg VGG-Face ArcFace OpenFace

#It takes a list of models but you can also pass one model if you want.
