import blurIris
import os

inputImage = os.path.dirname(os.path.realpath(__file__))+'/faceSampleImage/vSelfie.jpg'
blurIris.iris_blur(inputImage)