
"""
Haar-Cascade Algorithm
@author: Abdul Wasay Sardar, Zeeshan Khan and Hasnain Zia
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt
import time

start_time = time.time()
img = cv2.imread('pp.jpg')
person_csc = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_fullbody.xml")
persons = person_csc.detectMultiScale(img, 1.005, 15)
for (x,y,w,h) in persons:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
print("--- %s seconds ---" % (time.time() - start_time))
    #cv2.imshow("Haar Cascade Person Detection and Crowd Counting", img)
plt.imshow(img)
plt.show()


