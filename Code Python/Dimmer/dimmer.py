import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(12,GPIO.OUT)
pwm = GPIO.PWM(12,100)
pwm.start(0)



while True:
    persen = input('Input Persen PWM = ')
    p = float(persen)
    pwm.ChangeDutyCycle(p)