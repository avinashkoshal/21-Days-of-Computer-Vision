import cv2
face_cascade = cv2.CascadeClassifier('front_face.xml')
img = cv2.imread('im.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
#     crop =img[y:(y+h), x : (x+w)]  
# cv2.imshow('cropped image', crop)
cv2.waitKey(1)    
cv2.imshow('img', img)
# file='abc.png'
# cv2.imwrite('file.png',crop)
cv2.waitKey(0)
cv2.destroyAllWindows()