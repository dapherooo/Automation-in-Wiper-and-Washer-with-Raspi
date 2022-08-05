import cv2
import numpy as np

def nothing(x):
    pass

cam = cv2.VideoCapture(0)
cv2.namedWindow('Trackbars')
#cv2.resizeWindow("Trackbars", 1000, 125)
 
cv2.createTrackbar("L-H", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("L-S", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("L-V", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("U-H", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("U-S", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("U-V", "Trackbars", 0, 255, nothing)

while True:
    ret, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    l_h = cv2.getTrackbarPos("L-H", "Trackbars")
    l_s = cv2.getTrackbarPos("L-S", "Trackbars")
    l_v = cv2.getTrackbarPos("L-V", "Trackbars")
    u_h = cv2.getTrackbarPos("U-H", "Trackbars")
    u_s = cv2.getTrackbarPos("U-S", "Trackbars")
    u_v = cv2.getTrackbarPos("U-V", "Trackbars")

    #RGB Trackbar for detecting Contour with RGB Range
    color1 = np.array([l_h, l_s, l_v])
    color2 = np.array([u_h, u_s, u_v])
    color_mask1 = cv2.inRange(rgb_frame, color1, color2)
   
    color_mask = color_mask1
    
    _, contours, _ = cv2.findContours(color_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)

    for cnt in contours:
        (x, y, w, h) = cv2.boundingRect(cnt)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        break

    cv2.imshow('Frame', frame)
    cv2.imshow('Mask', color_mask)

    key = cv2.waitKey(1)
    if key == 27:
        break

cam.release()
cv2.destroyAllWindows()
