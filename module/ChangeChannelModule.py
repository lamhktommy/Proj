import re
moduleName = "ChangeChannelModule"

#All of the words must be heard in order for this module to be executed
commandWords = ["CHANNEL"]

def execute(command):
    #Write anything you want to be executed when the commandWords are heard
    #The 'command' parameter is the command you speak
	command=command.replace("CHANNEL ","")
	f=open('./module/channel.txt',"r")
	contents=f.read()
	contents=eval(contents)
	found=False
	for i in contents:
		for j in i:
			if j==command:
				found=True
				name=j
				break
	if not found:
		print("Channel "+command+" does not exist")
	else:
		print("Changed to channel "+name)