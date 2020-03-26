import cv2

video = cv2.VideoCapture(0)

while(True):
	ret,frame = video.read()
	cv2.imshow('result', frame)
	cv2.waitKey(1)
	if cv2.waitKey(33) == 27:
		break
cv2.destroyAllWindows()


