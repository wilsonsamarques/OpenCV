import numpy as np 
import cv2 

img  = cv2.imread('soccer_practice.jpg', 0)
template = cv2.imread('ball.png', 0)
h, w = template.shape


methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, 
           cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]


for method in methods:
	img2 = img.copy()


	result = cv2.matchTemplate(img2, template, method)
	#size of the output array -> (W - w + 1, H - h + 1)
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
	if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
		location = min_loc 
	else:
		location = max_loc 

	bottom_right = (location[0] + w, location[1] + h)
	cv2.rectangle(img2, location, bottom_right, 255, 5)
	cv2.imshow('Match', img2)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


# (3, 3)
# W = 4 
# w = 2 
# H = 4 
# h = 2 

# [[1, 1, 1],
#  [1, 1, 1], 
#  [1, 1, 1]]


# [[255, 255, 255, 255], 
#  [255, 255, 255, 255], 
#  [255, 255, 255, 255], 
#  [255, 255, 255, 255]]


# [[255, 255],
#  [255, 255]]






