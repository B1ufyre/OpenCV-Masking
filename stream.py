import cv2
webcam = cv2.VideoCapture(0)
while 1 == 1:
    ret, img = webcam.read()
    cv2.imshow("webcam.mp4", img)
    k = cv2.waitKey(10)
    if k == 27:
        break