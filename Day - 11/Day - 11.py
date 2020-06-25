import cv2

image = cv2.imread('a.png')
cv2.imshow("Image", image)
cv2.waitKey(0)

# convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)[1]
cv2.imshow("Thresh", thresh)
cv2.waitKey(0)

# we apply erosions to reduce the size of foreground objects
img = thresh.copy()
img = cv2.erode(img, None, iterations=5)
cv2.imshow("Eroded", img)
cv2.waitKey(0)

# similarly, dilations can increase the size of the ground objects
img = thresh.copy()
img = cv2.dilate(img, None, iterations=5)
cv2.imshow("Dilated", img)
cv2.waitKey(0)


cv2.imshow("Output", output)
cv2.waitKey(0)