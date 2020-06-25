import cv2
import numpy as np 

# Sketch generating function
def sketch(image):
	gray=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	# clean up image using Baussian Blur
	blur=cv2.GaussianBlur(gray, (5,5), 0)
	# Extract Edges 
	edges = cv2.Canny(blur, 10, 70)
	# invert binarize
	ret, mask=cv2.threshold(edges, 70, 255, cv2.THRESH_BINARY_INV)
	return mask
# initialize webcam
cap=cv2.VideoCapture(0)

while True:
	ret, frame=cap.read()
	cv2.imshow('original', frame)
	cv2.imshow('live Sketcher',sketch(frame))
	if cv2.waitKey(1) == 27:
		break

cap.release()
cv2.destroyAllWindows()