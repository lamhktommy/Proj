import paho.mqtt.client as mqtt
import time
hostname = "iot.eclipse.org" # Sandbox broker
port = 1883 # Default port for unencrypted MQTT


def on_connect(client, userdata, flags, rc):
	# Successful connection is '0'
	print("Connection result: " + str(rc))
	if rc == 0:
		# Subscribe to topics
		client.subscribe(topic)

def on_message(client, userdata, message):
	global h
	print("Received message on %s: %s (QoS = %s)" % 
		(message.topic, message.payload.decode("utf-8") , str(message.qos)))
	h=message.payload.decode("utf-8")



def on_disconnect(client, userdata, rc):
	if rc != 0:
		print("Disconnected unexpectedly")

global h
h=""
topic = "elec3542/Tommy/H" 
	# Initialize client instance
client = mqtt.Client()
	# Bind events to functions
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect

# Connect to the specified broker
client.connect(hostname, port, 60)

client.loop_start()
time.sleep(5)
print(h)
# Network loop runs in the background to listen to the events
client.loop_stop()


	# Wildcard '#' indicates that all sub-topics (e.g., elec3542/test, elec3542/sensor/temperature, etc.)

