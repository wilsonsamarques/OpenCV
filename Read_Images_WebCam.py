import cv2


# # Read an image
# img = cv2.imread("resources/lena.png")
# cv2.imshow("Lena", img)
# cv2.waitKey(0)


# Read a video 
frameWidth =  640 
frameHeight = 100


cap = cv2.VideoCapture("resources/testVideo.mp4")
#cap = cv2.VideoCapture(0)
# cap.set(3, frameWidth)
# cap.set(4, frameHeight)

while True:
    success, img = cap.read()
    img = cv2.resize(img,(frameWidth, frameHeight))
    cv2.imshow("Video", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break




