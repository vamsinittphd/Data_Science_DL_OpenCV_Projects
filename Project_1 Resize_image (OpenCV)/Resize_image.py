import cv2
import imutils
img = cv2.imread("Vamsi1.jpg")
img_resized = imutils.resize(img,width=20,height=20)
cv2.imwrite("Vamsi1_modified.jpg",img_resized)
