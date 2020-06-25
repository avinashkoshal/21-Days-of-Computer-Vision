import cv2

cap = cv2.VideoCapture('pedestrians.avi')
ped_cascade = cv2.CascadeClassifier('pedestrian.xml')

while True:
    ret, frame = cap.read()
    
    if (type(frame) == type(None)):
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ped = ped_cascade.detectMultiScale(gray,1.3,2)

    for(a,b,c,d) in ped:
        cv2.rectangle(frame,(a,b),(a+c,b+d),(0,255,210),4)
    
    cv2.imshow('video', frame)
    
    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()
