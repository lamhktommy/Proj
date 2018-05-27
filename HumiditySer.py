import paho.mqtt.publish as publish
from sense_hat import SenseHat
import time

hostname = "iot.eclipse.org" # Sandbox broker
port = 1883 # Default port for unencrypted MQTT
sense = SenseHat()

sense.show_message("Hello User!",scroll_speed=0.05)

h=sense.get_humidity()
h=round(h,1)

message=str(h)+"%"+" "
sense.show_message(message, scroll_speed=0.05)
htopic= "elec3542/Tommy/H"

# API reference can be found at https://eclipse.org/paho/clients/python/docs/#id17
while True:
	publish.single(htopic, payload=message, qos=0,hostname=hostname,port=port)
	print(message)
	time.sleep(5)
	sense.show_message(message, scroll_speed=0.05)