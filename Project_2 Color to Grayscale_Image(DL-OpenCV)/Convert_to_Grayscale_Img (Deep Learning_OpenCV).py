import cv2
import imutils
img = cv2.imread("Vamsi1.jpg")

#This code will smooths the image
gaussianBlurImg = cv2.GaussianBlur(img,(50,60),0)
cv2.imwrite("Vamsi1_smoothed.jpg",gaussianBlurImg)

#This code will convert an image to grayscale image
grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
threshImg = cv2.threshold(grayImg,80,120,cv2.THRESH_BINARY)[1]
cv2.imwrite("Vamsi1_grayscale.jpg",threshImg)
