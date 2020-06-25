import cv2 

img = cv2.imread('a.png') 
cv2.imshow('original',img)
mask = cv2.imread('a_m.png', 0) 
cv2.imshow('mask',mask)
ns = cv2.inpaint(img, mask, 1, cv2.INPAINT_NS) 
telea = cv2.inpaint(img, mask, 1, cv2.INPAINT_TELEA) 

cv2.imshow('ns',ns)
cv2.imshow('telea',telea)
cv2.waitKey(0)
cv2.destroyAllWindows()
