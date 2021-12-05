def iris_blur(image_file_name) :
    import cv2
    import numpy as np
    import matplotlib.pyplot as plt
    import math
    import os

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    outputImage = os.path.dirname(os.path.realpath(__file__))+'/protectedImage/new.jpg'

    img = cv2.imread(image_file_name)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ksize = 10
    tmp = 0

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        roi_color = img[y:y + h, x:x + w]
        roi_gray = gray[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            p1 = (x+ex+5, y+ey)
            p2 = (p1[0] + ew, p1[1] + eh)

            circle_center = ((p1[0] + p2[0])// 2, (p1[1] + p2[1]) // 2)
            circle_radius = int(math.sqrt(ew*2 + eh*2) // 2)
            mask_img = np.zeros(img.shape, dtype='uint8')
            cv2.circle(mask_img, circle_center, circle_radius, (255, 255, 255), -1)

            img_all_blurred = cv2.blur(img, (ksize, ksize))

            if tmp == 0:
                img_first_blurred = np.where(mask_img > 0, img_all_blurred, img)
                tmp += 1
            
            else :
                img_second_blurred = np.where(mask_img > 0, img_all_blurred, img_first_blurred)
                tmp += 2

    if tmp == 1:
        cv2.imwrite(outputImage,img_first_blurred)

    elif tmp == 2:
        cv2.imwrite(outputImage,img_second_blurred)

    else :
        cv2.imwrite(outputImage,img)

    
if __name__ == '__main__':
    iris_blur()