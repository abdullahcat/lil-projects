import cv2
import time
import numpy as np

thing_cascade=cv2.CascadeClassifier('haarcascade.xml')

cam=cv2.VideoCapture(0)

while True:
    _,frame=cam.read()
    bw=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    face=thing_cascade.detectMultiScale(bw,scaleFactor=1.1,minNeighbors=5)
    for x,y,w,h in face:
        img=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),1)
        img[y:y+h,x:x+w]=cv2.medianBlur(img[y:y+h,x:x+w],35)
    
    cv2.imshow("Frame", frame)
    key=cv2.waitKey(1)

    if key==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
