import face_recognition
import pathlib
def face_rec():
	image = face_recognition.load_image_file("./capture_pic/2018-05-25_15:51:48.jpg")
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
	unknown_img = face_recognition.load_image_file("./capture_pic/2018-05-25_15:51:48.jpg")
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
	print(results)
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

face_rec()