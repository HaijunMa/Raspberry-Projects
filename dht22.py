'''
Title:DHT22
@author:Haijun Ma
Time:2018/11/19
'''

#!/usr/bin/python
import Adafruit_DHT
sensor = Adafruit_DHT.DHT22
pin = 4  #GPIO4
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
else:
    print('Failed to get reading. Try again!')