import json, time
import urequests as requests
from machine import Pin, ADC
from time import sleep
import network

ledV = Pin(25,Pin.OUT)
ledR = Pin(26,Pin.OUT)
ledW = Pin(2,Pin.OUT)
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('RD','cumboy123')

while True:
 WC = wlan.isconnected()
 if (WC == True):
     ledW.value(1)
 if (WC == False):
     ledW.value(0)    
 
 try:
  consulta = requests.get("https://thingspeak.com/channels/2328045/feeds.json?results=1")
  data = consulta.json()
  print("consultado")
  valor= float(data["feeds"][0]["field1"])
  if (valor > 1.65):
     ledV.value(0)
     ledR.value(1)
  if (valor<1.65):
      ledV.value(1)
      ledR.value(0)
 except:
     print("fallo")

 time.sleep (0.5)