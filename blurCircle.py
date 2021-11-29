import cv2
import matplotlib.pyplot as plt
import numpy as np
import math

img = cv2.imread('noze.jpg')
h, w, c = img.shape

p1 = (h, w)     # 블러생성 위치
w, h = 100, 100
p2 = (p1[0] + w, p1[1] + h)        #블러 끝나는 위치

circle_center = ((p1[0] + p2[0])// 2, (p1[1] + p2[1]) // 2)
circle_radius = int(math.sqrt(w * w + h * h) // 2)
mask_img = np.zeros(img.shape, dtype='uint8')
cv2.circle(mask_img, circle_center, circle_radius, (255, 255, 255), -1)

img_all_blurred = cv2.medianBlur(img, 99)
img_face_blurred = np.where(mask_img > 0, img_all_blurred, img)

cv2.imshow("Detected Circle", img_face_blurred)
cv2.waitKey(0)