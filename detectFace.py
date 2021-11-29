import cv2
import numpy as np
import matplotlib.pylab as plt
import math

# haarcascade 불러오기
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# 이미지 불러오기
img = cv2.imread('noze3.jpg')
# mask = cv2.imread('eyeBlurMask.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ksize = 10
tmp = 0
# 합성할 마스크 전체 영역을 255로 셋팅??
# maskArea = np.full_like(mask, 255)

# 얼굴 찾기
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x, y, w, h) in faces:
    # cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    # 눈 찾기
    roi_color = img[y:y + h, x:x + w]
    roi_gray = gray[y:y + h, x:x + w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        # cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

        p1 = (x+ex+5, y+ey)     # 블러생성 위치
        p2 = (p1[0] + ew, p1[1] + eh)        #블러 끝나는 위치

        circle_center = ((p1[0] + p2[0])// 2, (p1[1] + p2[1]) // 2)
        circle_radius = int(math.sqrt(ew*2 + eh*2) // 2)        # 블러 크기
        mask_img = np.zeros(img.shape, dtype='uint8')
        cv2.circle(mask_img, circle_center, circle_radius, (255, 255, 255), -1)

        img_all_blurred = cv2.blur(img, (10, 10))   # 블러 수치

        if tmp == 0:
            img_first_blurred = np.where(mask_img > 0, img_all_blurred, img)
            tmp += 1

        if tmp == 1:
            img_second_blurred = np.where(mask_img > 0, img_all_blurred, img_first_blurred)

    cv2.imshow("Detected Circle", img_second_blurred)
cv2.waitKey(0)