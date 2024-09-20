import cv2
import numpy
green = cv2.VideoCapture(0)
bg = 0
for i in range(60):
    ret, bg = green.read()
while 1 == 1:
    ret, img = green.read()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_red = numpy.array([100,40,40])
    upper_red = numpy.array([100, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    lower_red2 = numpy.array([150,40,40])
    upper_red2 = numpy.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = mask1 + mask2
    mask3 = cv2.morphologyEx(mask, cv2.MORPH_OPEN, numpy.ones((3,3), numpy.uint8), iterations = 2)
    mask4 = cv2.dilate(mask3, numpy.ones((3,3), numpy.uint8), iterations = 1)
    mask5 = cv2.bitwise_not(mask4)
    result1 = cv2.bitwise_and(bg, bg, mask = mask4)
    result2 = cv2.bitwise_and(img, img, mask = mask5)
    result3 = cv2.addWeighted(result1, 1, result2, 1, 0)
    cv2.imshow("green.mp4", mask5)
    k = cv2.waitKey(10)
    if k == 27:
        break