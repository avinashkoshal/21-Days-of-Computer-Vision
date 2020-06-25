import cv2

image = cv2.imread('jp.png')
cv2.imshow('original',image)

b = image.copy()
# set green and red channels to 0
b[:, :, 1] = 0
b[:, :, 2] = 0

                                                       
g = image.copy()                                        0      1      2
# set blue and red channels to 0                        B      G      R
g[:, :, 0] = 0                                      
g[:, :, 2] = 0

r = image.copy()
# set blue and green channels to 0
r[:, :, 0] = 0
r[:, :, 1] = 0


# RGB - Blue
cv2.imshow('Blue', b)

# RGB - Green
cv2.imshow('Green', g)

# RGB - Red
cv2.imshow('Red', r)

cv2.waitKey(0)