import cv2 

# Reading Image
image = cv2.imread('3.png') 
cv2.imshow('original Image', image)
cv2.waitKey(0) 

# Grayscale 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
cv2.imshow('gray',gray)
cv2.waitKey(0)

# Find Canny edges 
edged = cv2.Canny(gray, 30, 200) 
cv2.imshow('edged Image',edged)
cv2.waitKey(0) 

# Finding Contours 
contours, hierarchy = cv2.findContours(edged, 
	cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  #Contour Retrieval Mode,   stores absolutely all the contour points.
#https://docs.opencv.org/3.4/d9/d8b/tutorial_py_contours_hierarchy.html

number=str(len(contours))

# Draw all contours 
# -1 signifies drawing all contours 
cv2.drawContours(image, contours, -1, (0, 255, 0), 3) 
cv2.putText(image, "Number of contours = " + number, (10, 25), 
	cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255	), 2)

cv2.imshow('Contours', image) 
cv2.waitKey(0) 
cv2.destroyAllWindows() 
