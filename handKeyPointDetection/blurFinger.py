def Finger_blur(inputImage) :
    import handPoseImage
    import cv2
    import numpy as np
    import matplotlib.pyplot as plt
    import math
    import os

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    outputImage = os.path.dirname(os.path.realpath(__file__))+'/protectedImage/new.jpg'

    img = cv2.imread(inputImage)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ksize = 10

    # points = [handPoseImage.detect_fingerPoint()[0], handPoseImage.detect_fingerPoint()[1], handPoseImage.detect_fingerPoint()[2], handPoseImage.detect_fingerPoint()[3]]
    points = handPoseImage.detect_fingerPoint(inputImage)

    p1 = points[0]  # 4번좌표
    p2 = points[1]  # 5번좌표
    p3 = points[2]  # 8번좌표
    p4 = points[3]  # 7번좌표
    mask_img = np.zeros(img.shape, dtype='uint8')
    
    # 검지
    circle_center = ((p1[0] + p2[0]) // 2, (p1[1] + p2[1]) // 2)
    # circle_radius = abs(int((p1[1] - p2[1]) // 4))
    circle_radius = int((math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2))//3)

    print(circle_center)
    print(circle_radius)
    cv2.circle(mask_img, circle_center, circle_radius, (255, 255, 255), -1)

    img_all_blurred = cv2.blur(img, (ksize, ksize))
    img_first_blurred = np.where(mask_img > 0, img_all_blurred, img)

    # 중지
    circle_center = ((p3[0] + p4[0]) // 2, (p3[1] + p4[1]) // 2)
    # circle_radius = abs(int((p3[1] - p4[1]) // 4))
    circle_radius = int((math.sqrt((p3[0]-p4[0])**2 + (p3[1]-p4[1])**2))//5)

    cv2.circle(mask_img, circle_center, circle_radius, (255, 255, 255), -1)

    img_second_blurred = np.where(mask_img > 0, img_all_blurred, img_first_blurred)

    cv2.imwrite(outputImage, img_second_blurred)
    
if __name__ == '__main__':
    Finger_blur()