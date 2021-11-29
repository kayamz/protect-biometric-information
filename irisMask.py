import cv2
import numpy as np
import matplotlib.pylab as plt

# haarcascade 불러오기
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# 이미지 불러오기
img = cv2.imread('face.jpg')
mask = cv2.imread('eyeBlurMask.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 합성할 마스크 전체 영역을 255로 셋팅??
maskArea = np.full_like(mask, 5000)

# 얼굴 찾기
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x, y, w, h) in faces:
    # cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    # 눈 찾기
    roi_color = img[y:y + h, x:x + w]
    roi_gray = gray[y:y + h, x:x + w]
    #홍채 영역 지정
    # roi_iris = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

        

# print(ex, ey, ew, eh)
# 마스크 합성 좌표 계산 (눈의 중앙)
# iris = ((2*ex+ew)//2, (2*ey+eh)//2)

# print(iris)

# seamlessClone 으로 합성
# normal = cv2.seamlessClone(mask, img, maskArea, iris, cv2.NORMAL_CLONE)
# mixed = cv2.seamlessClone(mask, img, maskArea, iris, cv2.MIXED_CLONE)

# 이미지 출력
# cv2.imshow('image', img)
cv2.imshow('normal', normal)
# cv2.imshow('mixed', mixed)
cv2.waitKey()
# key = cv2.waitKey(0)
cv2.destroyAllWindows()