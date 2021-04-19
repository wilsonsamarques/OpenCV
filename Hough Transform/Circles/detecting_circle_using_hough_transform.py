import numpy as np 
import cv2

img = cv2.imread('circle.png')
#img = cv2.imread('circles.jpg')
#img = cv2.imread('circles_2.jpg')
#img = cv2.imread('furo_escareado.jpg') # does not work, probably because of the inclination
#img = cv2.imread('furo_escareado_cad.png')
#img = cv2.imread('furo_escareado_cad_perpendicular.png')
#img = cv2.imread('furo_escareado_2.jpg') # does not work, probably because of the inclination
#img = cv2.imread('furo_escareado_3.jpg') # does not work, probably because of the inclination
#img = cv2.imread('furo_escareado_madeira_perpendicular.jpg')

output = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, 
                           param1=0, param2=30, minRadius=0, maxRadius=0)

detected_circles = np.uint16(np.around(circles))
for (x, y, r) in detected_circles[0, :]:
    cv2.circle(output, (x, y), r, (0, 255, 0), 3)
    cv2.circle(output, (x, y), 2, (0, 255, 255), 3)


cv2.putText(output, "Diameter: {:.2f}".format(r), (10,30), cv2.FONT_HERSHEY_COMPLEX,1,(0,200,0),1)
cv2.imshow('output', output)
cv2.imshow('median blur', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
