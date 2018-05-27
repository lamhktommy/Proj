import paho.mqtt.client as mqtt
#You can import any required modules here

#This can be anything you want
moduleName = "WeatherModule"

#All of the words must be heard in order for this module to be executed
commandWords = ["weather"]


global hostname,port,topic,temperature
temperature=""
hostname = "iot.eclipse.org" # Sandbox broker
port = 1883 # Default port for unencrypted MQTT
topic="elec3542/Tommy/#"

def on_connect(client, userdata, flags, rc):
	global topic# Successful connection is '0'
	print("Connection result: " + str(rc))
	if rc == 0:
		# Subscribe to topics
		client.subscribe(topic)

def on_message(client, userdata, message):
	global temperature
	print("Received message on %s: %s (QoS = %s)" % 
		(message.topic, message.payload.decode("utf-8") , str(message.qos)))
	temperature=message.payload.decode("utf-8")



def on_disconnect(client, userdata, rc):
	if rc != 0:
		print("Disconnected unexpectedly")


def execute(command):
    #Write anything you want to be executed when the commandWords are heard
    #The 'command' parameter is the command you speak

	client = mqtt.Client()
	# Bind events to functions
	client.on_connect = on_connect
	client.on_message = on_message
	client.on_disconnect = on_disconnect
		# Connect to the specified broker
	client.connect(hostname, port, 60)

	client.loop_start()
	time.sleep(5)

	# Network loop runs in the background to listen to the events
	client.loop_stop()
	print(temperature)