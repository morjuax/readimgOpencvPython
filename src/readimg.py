import cv2

img = cv2.imread('./img/opencv_logo.png', 0)
cv2.imshow('Prueba de imagen', img)
cv2.imwrite('./img/gray.jpg', img) #save
cv2.waitKey(0)
cv2.destroyAllWindows()
