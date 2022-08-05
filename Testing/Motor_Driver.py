import RPi.GPIO as GPIO
from time import sleep

x_medium = 0


class Motor():
    def __init__(self, in1, in2):
        self.in1 = in1
        self.in2 = in2
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.in1, GPIO.OUT)
        GPIO.setup(self.in2, GPIO.OUT)


    def turun(self, x=50, t=0):
        self.p = GPIO.PWM(self.in1, 1000)  # Frequency in Hz
        self.p.start(0)  # DutyCycle
        GPIO.output(self.in2, GPIO.LOW)
        self.p.ChangeDutyCycle(x)
        # print('MOVE TO RIGHT')
        sleep(t)

    def naik(self, x=50, t=0):
        self.p = GPIO.PWM(self.in2, 1000)  # Frequency in Hz
        self.p.start(0)  # DutyCycle
        GPIO.output(self.in1, GPIO.LOW)
        self.p.ChangeDutyCycle(x)
        # print('MOVE TO LEFT')
        sleep(t)

    def stop(self):
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.LOW)
        self.p.ChangeDutyCycle(0)
        # print('NOT MOVING')


motor1 = Motor(16, 12) # D0 D1
motor2 = Motor(20, 21) # D2 D3

motor1.turun(70, 3)
motor1.naik(70, 3)
motor2.turun(65, 5)
motor1.stop()
motor2.stop()

GPIO.cleanup()

