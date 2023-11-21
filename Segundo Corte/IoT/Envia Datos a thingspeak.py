import json, time
import urequests as requests
from machine import Pin, ADC
from time import sleep
import network

ledV = Pin(25,Pin.OUT)
ledR = Pin(26,Pin.OUT)
ledW = Pin(2,Pin.OUT)
wlan = network.WLAN(network.STA_IF)
pot = ADC(Pin (35))
pot.atten(ADC.ATTN_11DB)
url = "https://api.thingspeak.com/update?api_key=9ZEZOU7T2U1OJKOR&field1=%s"

wlan.active(True)
wlan.connect('RD','cumboy123')

while True:
 WC = wlan.isconnected()
 if (WC == True):
     ledW.value(1)
 if (WC == False):
     ledW.value(0)    
     
 
 pot_valor = pot.read()
 voltaje = (3.3/4095)*pot_valor 
 print (voltaje)
 data = url % str(voltaje)
 try:
   res = requests.get(data)
   print("publicado\n")
   ledV.value(1)
   ledR.value(0)
 except:
   print("fallo\n")
   ledV.value(0)
   ledR.value(1)

 time.sleep (0.5)
