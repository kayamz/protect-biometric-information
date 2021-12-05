# import blurFinger
# import os

# inputImage = os.path.dirname(os.path.realpath(__file__))+'/faceSampleImage/vSign.jpg'
# blurFinger.Finger_blur(inputImage)


import handPoseImage
import os

inputImage = os.path.dirname(os.path.realpath(__file__))+'/handSampleImage/vSign.jpg'
handPoseImage.detect_fingerPoint(inputImage)