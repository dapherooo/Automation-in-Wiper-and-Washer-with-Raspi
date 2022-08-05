import cv2
import numpy as np
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(26, GPIO.OUT) # ubah pin yang digunakan D0
GPIO.setup(19, GPIO.OUT) # ubah pin yang digunakan D1
GPIO.setup(13, GPIO.OUT) # ubah pin yang digunakan D2
GPIO.setup(6, GPIO.OUT) # ubah pin yang digunakan D3
       

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # ubah angka array sesuai kalibrasi kaca yang di dapat (kaca)
    color1 = np.array([0, 68, 152])          
    color2 = np.array([167, 156, 255])
    color_mask = cv2.inRange(rgb_frame, color1, color2)
    
    
    _, contours, _ = cv2.findContours(color_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)
        
    for cnt in contours:
        (x, y, w, h) = cv2.boundingRect(cnt)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        break
    
    cv2.imshow('Frame',frame) #menampilkan frame
    #cv2.imshow('Mask', color_mask)
    print("outputx = "+str(x)) # menjadi parameter treshold yng digunakan setelah proses opencv untuk mendeteksi benda lain selain kaca
       
    key = cv2.waitKey(1)
    if key == 27:
        break
        
    if x <= 300: # batas bawah
     print("clean up")
     
     p = GPIO.PWM(13, 1000)  # ubah pin 13 dengan yang digunakan 
     p.start(0)  
     GPIO.output(6, GPIO.LOW)  # ubah pin 16 dengan yang digunakan
     p.ChangeDutyCycle(20)  #pwm
     sleep(1)
    
     p = GPIO.PWM(26, 1000)  
     p.start(0)  
     GPIO.output(19, GPIO.LOW)
     p.ChangeDutyCycle(20)
     sleep(1)
     
     p = GPIO.PWM(19, 1000)  
     p.start(0)  
     GPIO.output(26, GPIO.LOW)
     p.ChangeDutyCycle(20)
     sleep(1)
     
     p.stop()
     GPIO.output(26, GPIO.LOW)
     GPIO.output(19, GPIO.LOW)
     GPIO.output(13, GPIO.LOW)
     GPIO.output(6,  GPIO.LOW)
     
     
    elif x >= 450: #batas atas beda 150 dengan yg bawah
     print("clean up") 
     p = GPIO.PWM(13, 1000)  
     p.start(0)  
     GPIO.output(6, GPIO.LOW)
     p.ChangeDutyCycle(20)
     sleep(1)
     
     p = GPIO.PWM(26, 1000)  
     p.start(0)  
     GPIO.output(19, GPIO.LOW)
     p.ChangeDutyCycle(20)
     sleep(1)
     
     p = GPIO.PWM(19, 1000)  
     p.start(0)  
     GPIO.output(26, GPIO.LOW)
     p.ChangeDutyCycle(20)
     sleep(1)
      
     p.stop()
     GPIO.output(26, GPIO.LOW)
     GPIO.output(19, GPIO.LOW)
     GPIO.output(13, GPIO.LOW)
     GPIO.output(6,  GPIO.LOW)
     
    else:
     print("stay")
     GPIO.output(26, GPIO.LOW)
     GPIO.output(19, GPIO.LOW)
     GPIO.output(13, GPIO.LOW)
     GPIO.output(6,  GPIO.LOW)

    
GPIO.cleanup()
cam.release()
cv2.destroyAllWindows()

 
