import cv2 
import numpy as np 
import utils

webcam = True
path = 'resources/rectangles.jpg'
cap = cv2.VideoCapture(0)
cap.set(10,160)
cap.set(3,1920)
cap.set(4,1080)
scale = 3 
wP = 210 * scale
hP = 297 * scale

while True:
    if webcam: success, img = cap.read()
    else: img = cv2.imread(path)

    imgContours, conts = utils.getContours(img,minArea=50000,filter=4)

    if len(conts) != 0:
        biggest = conts[0][2]
        print(biggest)
        imgWarp = utils.warpImg(img,biggest, wP, hP)
        imgContours2, conts2 = utils.getContours(img,minArea=50000,filter=4,
                                        cThr=[50,50],draw=False)


        if len(conts2) != 0:
            for obj in conts2:
                cv2.polylines(imgContours2,[obj[2]],True,(0,255,0),2)
        cv2.imshow('A4', imgContours2)

    img = cv2.resize(img,(0,0), None, 0.5, 0.5)
    cv2.imshow('Original', img)
    cv2.waitKey(1)
