from gpiozero import MCP3008
from time import sleep

getar = MCP3008(0)

while True:
    adc = (getar.value)*1023
    print(adc)
    sleep(0.5)