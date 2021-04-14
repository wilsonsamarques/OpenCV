import cv2 

path = "resources/road.jpg"

img = cv2.imread(path)

print(img.shape)

width, height = 1000, 1000
imgResize = cv2.resize(img, (width, height))
print(imgResize.shape)

imgCropped = img[300:659,430:500]

imgCroppedResize = cv2.resize(imgCropped,(img.shape[1], img.shape[0]))


cv2.imshow("Road", img)
cv2.imshow("Road resized", imgResize)
cv2.imshow("Road cropped", imgCropped)
cv2.imshow("Road cropped resized", imgCroppedResize)

cv2.waitKey(0)

