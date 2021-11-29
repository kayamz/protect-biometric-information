import cv2
import numpy as np
import math
  
# Read image.
img = cv2.imread('face.jpg', cv2.IMREAD_COLOR)
  
# Convert to grayscale.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  
# Blur using 3 * 3 kernel.
gray_blurred = cv2.blur(gray, (3, 3))
  
# 블러 수치
ksize = 100

# Apply Hough transform on the blurred image.
detected_circles = cv2.HoughCircles(gray_blurred, 
                   cv2.HOUGH_GRADIENT, 1, 20, param1 = 50,
               param2 = 30, minRadius = 1, maxRadius = 40)
  
# Draw circles that are detected.
if detected_circles is not None:
  
    # Convert the circle parameters a, b and r to integers.
    detected_circles = np.uint16(np.around(detected_circles))
  
    for pt in detected_circles[0, :]:
        a, b, r = pt[0], pt[1], pt[2]
  
        # Draw the circumference of the circle.
        cv2.circle(img, (a, b), r, (0, 255, 0), 2)
  
        # Draw a small circle (of radius 1) to show the center.
        cv2.circle(img, (a, b), 1, (0, 0, 255), 3)

        # 블러처리
        p1 = (140, 225)     # 블러생성 위치
        w, h = 100, 100
        p2 = (p1[0] + w, p1[1] + h)        #블러 끝나는 위치

        circle_center = ((p1[0] + p2[0])// 2, (p1[1] + p2[1]) // 2)
        circle_radius = int(math.sqrt(w * w + h * h) // 2)
        mask_img = np.zeros(img.shape, dtype='uint8')
        cv2.circle(mask_img, circle_center, circle_radius, (255, 255, 255), -1)

        img_all_blurred = cv2.medianBlur(img, 99)
        img_face_blurred = np.where(mask_img > 0, img_all_blurred, img)

        # 여기 위까지 수정

        cv2.imshow("Detected Circle", img)
        cv2.waitKey(0)