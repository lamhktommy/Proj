import face_recognition
import pathlib

def face_rec(picname):
	image = face_recognition.load_image_file("./capture_pic/"+picname+".jpg")
	face_locations = face_recognition.face_locations(image)
	if len(face_locations)==0:
		print("No Face Detected")
		os.remove("./capture_pic/"+picname+".jpg")
		return
	#for i in face_locations:
	#	face_locations=(i[3],i[0],i[1],i[2])
	#print("Face Detected at "+face_locations)	
	currentDirectory = pathlib.Path('./known_face')
		# define the pattern
	currentPattern = "*.jpg"
	mylist=list(currentDirectory.glob(currentPattern))
	#print(mylist)
	for image in mylist:
		#print(str(image))
		known_img=face_recognition.load_image_file(image)
		unknown_img = face_recognition.load_image_file("./capture_pic/"+picname+".jpg")
		try:
			known_face_encoding = face_recognition.face_encodings(known_img)[0]
			unknown_face_encoding = face_recognition.face_encodings(unknown_img)[0]
		except IndexError:
		    print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
		    quit()
		known_faces = [known_face_encoding]
		results = face_recognition.compare_faces(known_faces, unknown_face_encoding)
		if (True in results):
			print(str(image)+" Detected!!!!")

face_rec("2018-05-24_03:52:28")