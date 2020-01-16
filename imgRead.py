import cv2

img = cv2.imread(r'FB_IMG_1502720974277.JPG',0)

print(img)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindow
