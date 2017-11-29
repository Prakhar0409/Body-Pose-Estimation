import cv2
import numpy as np 

# cap = cv2.VideoCapture(0)

# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

# while True:
# 	ret, frame = cap.read()
# 	cv2.imshow('frame', frame)

# 	out.write(frame)
# 	if (cv2.waitKey(33) & 0xFF) == 27:
# 		break

# cap.release()
# out.release()
# cv2.destroyAllWindows()

# --------------------------------------------------

# img1 = cv2.imread('3D-Matplotlib.png')
# img2 = cv2.imread('mainsvmimage.png')

# # add = img1 + img2
# # add = cv2.add(img1,img2)
# add = cv2.addWeighted(img1,0.6,img2,0.4,0)

# cv2.imshow('img1', img1)
# cv2.imshow('img2', img2)
# cv2.imshow('add', add)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


# --------------------------------------------------

img1 = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('mainlogo.png')

rows,cols,channels = img2.shape
roi = img1[0:rows,0:cols]

img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

# pixel values above 220 will be convereted to 255 
# and below 220 is converted to 0. THRES_BINARY_INV flips it because it is inverse
ret,mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)

cv2.imshow('gray',img2gray)
cv2.imshow('mask',mask)

cv2.waitKey(0)
cv2.destroyAllWindows()
