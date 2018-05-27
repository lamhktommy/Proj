from picamera import PiCamera
import pathlib
import os 
import face_recognition
import time
print("------------------------------------------------------------------------")
print("|                            New User Setup                            |")
print("|                  Thank you for choosing Potato Inc.                  |")
print("------------------------------------------------------------------------")
name=input("Input your name: ")

currentDirectory = pathlib.Path('./known_face/')
		# define the pattern
currentPattern = "*.jpg"
mylist=list(currentDirectory.glob(currentPattern))
camera = PiCamera() #if no memory sudo rpi-update, memory-split, reboot
camera.rotation = 180
camera.capture("./known_face/"+name+".jpg")
image = face_recognition.load_image_file("./known_face/"+name+".jpg")
face_locations = face_recognition.face_locations(image)
while len(face_locations)==0:
	print("No face detected!")
	print("Take another in 5 sec")
	os.remove("./known_face/"+name+".jpg")
	for i in range(5):
		print(i)
		time.sleep(1)
	camera.capture(name+".jpg")
	face_locations = face_recognition.face_locations(image)
print(face_locations)