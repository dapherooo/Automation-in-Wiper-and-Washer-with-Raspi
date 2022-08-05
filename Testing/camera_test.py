import cv2

cam = cv2.VideoCapture(0)

while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cv2.imshow('frame', frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
    
cam.release()
cv2.destroyAllWindows()
    
    