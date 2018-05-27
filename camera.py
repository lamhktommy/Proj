from picamera import PiCamera
from time import sleep
import datetime 
import pathlib
import threading
import os 
import face_recognition
from PIL import Image
from re import search

class get_latest (threading.Thread):
	def run(self):
		currentDirectory = pathlib.Path('.//capture_pic')
		# define the pattern
		currentPattern = "*.jpg"
		mylist=list(currentDirectory.glob(currentPattern))
		mylist.sort(reverse=True)
		if (len(mylist)>0):
			latest_pic=mylist[0]
			print("Latest_pic: "+str(latest_pic))
			s=str(latest_pic)
			match= search('[0-9]{4}-[0-9]{2}-[0-9]{2}_[0-9]{2}:[0-9]{2}:[0-9]{2}', s)
			date=match.group(0)
			face_rec(str(date))
		else:
			print("Folder is empty")

def face_rec(picname):
	image = face_recognition.load_image_file("./capture_pic/"+picname+".jpg")
	face_locations = face_recognition.face_locations(image)
	if len(face_locations)==0:
		print("No Face Detected")
		return
	#for i in face_locations:
	#	face_locations=(i[3],i[0],i[1],i[2])
	#print("Face Detected at "+face_locations)	
	currentDirectory = pathlib.Path('./known_face')
		# define the pattern
	currentPattern = "*.jpg"
	mylist=list(currentDirectory.glob(currentPattern))
	#print(mylist)
	unknown_img = face_recognition.load_image_file("./capture_pic/"+picname+".jpg")
	unknown_face_encoding = face_recognition.face_encodings(unknown_img)[0]
	known_faces = []
	facename=[]
	for image in mylist:
		#print(str(image))
		known_img=face_recognition.load_image_file(image)
		known_face_encoding = face_recognition.face_encodings(known_img)[0]
		known_faces.append(known_face_encoding)
		facename.append(image)
	results = face_recognition.compare_faces(known_faces, unknown_face_encoding)
	found=False
	for i in range(len(results)):
		if (results[i]==True):
			global name
			name=str(facename[i])
			print(str(facename[i])+" Detected!!!!")
			found=True
	if not found:
		print("New face detected")
	else:
		print("Name: "+str(name)+"")

def get_eldest():
	currentDirectory = pathlib.Path('.//capture_pic')
	# define the pattern
	currentPattern = "*.jpg"
	mylist=list(currentDirectory.glob(currentPattern))
	mylist.sort()
	eldest_pic="./"+str(mylist[0])
	print("eldest_pic: "+str(eldest_pic))
	return eldest_pic

def delete_eldest():
	eldest_pic=get_eldest()
	os.remove(eldest_pic)
	print(eldest_pic+" deleted!!!!")

def capture_pic():
	global camera
	now=datetime.datetime.now()
	now=now.strftime("%Y-%m-%d_%H:%M:%S")
	camera.capture('./capture_pic/'+str(now)+'.jpg')
	print('./capture_pic/'+str(now)+'.jpg captured!!!!')

i=0
global camera 
camera = PiCamera() #if no memory sudo rpi-update, memory-split, reboot
camera.rotation = 180
latestThread=get_latest()
while True:
	capture_pic()
	latestThread.run()
	i+=1
	if (i%5==0):
		for j in range(5):
				delete_eldest()