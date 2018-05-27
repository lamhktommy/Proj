from sense_hat import SenseHat

sense = SenseHat()
humidity = sense.get_humidity()
humidity=round(humidity,1)


message=str(humidity)+"%"+" "
print(message)
sense.show_message(message, scroll_speed=0.05)