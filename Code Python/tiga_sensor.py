from gpiozero import MCP3008
from time import sleep

getar1 = MCP3008(0)
getar2 = MCP3008(1)
getar3 = MCP3008(2)

while True:
    adc1 = (getar1.value)*1023
    adc2 = (getar2.value)*1023
    adc3 = (getar3.value)*1023

    print("Nilai Sensor 1 = " , adc1)
    print("Nilai Sensor 2 = " , adc2)
    print("Nilai Sensor 3 = " , adc3)
    print(" ")

    sleep(0.5)