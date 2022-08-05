import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
ENA,IN1,IN2 = 21,16,20

GPIO.setup(ENA,GPIO.OUT)
GPIO.setup(IN1,GPIO.OUT)
GPIO.setup(IN2,GPIO.OUT)
pwm = GPIO.PWM(ENA,100)
pwm.start(0)


while True:
    
    GPIO.output(IN1,GPIO.HIGH)
    GPIO.output(IN2,GPIO.LOW)
    pwm.ChangeDutyCycle(100)

    sleep(5)

    GPIO.output(IN1,GPIO.LOW)
    GPIO.output(IN2,GPIO.LOW)
    pwm.ChangeDutyCycle(0)

    sleep(5)

    GPIO.output(IN1,GPIO.HIGH)
    GPIO.output(IN2,GPIO.LOW)
    pwm.ChangeDutyCycle(60)

    sleep(5)

    GPIO.output(IN1,GPIO.LOW)
    GPIO.output(IN2,GPIO.LOW)
    pwm.ChangeDutyCycle(0)

    sleep(5)
GPIO.cleanup()
