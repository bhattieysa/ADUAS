import numpy as np
import cv2
import imutils
from datetime import datetime

# gun_cascade = cv2.CascadeClassifier('cascade.xml')
gun_cascade = None
try:
    # gun_cascade = cv2.CascadeClassifier('cascade.xml')
    gun_cascade = cv2.CascadeClassifier('knifecascade.xml')
except cv2.error as e:
    print("OpenCV Error:", e)
camera = cv2.VideoCapture(0)

first_frame = None
gun_exists = None

while True:
    ret, frame = camera.read()
    frame = imutils.resize(frame, width = 500)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    gun = gun_cascade.detectMultiScale(gray, 
                                       1.3,
                                       5 , 
                                       minSize=(100,100))
    

    if len(gun) > 0:
        gun_exists = True

    for (x,y,w,h) in gun:
        frame = cv2.rectangle(frame, (x,y) , (x+w, y + h), (255,0,0) , 2)
        roi_gray = gray[y:y+h , x : x + w]
        roi_color = frame[y:y+h , x : x + w]

    if first_frame is None:
        first_frame = gray
        continue
    cv2.imshow('Security Feed' , frame)
    key = cv2.waitKey(1) & 0XFF
    if key == ord('q'):
        break
if gun_exists:
    print('Gun exists')
else:
    print('Gun not found')
camera.release()
cv2.destroyAllWindows()

        
