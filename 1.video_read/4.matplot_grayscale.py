#!/usr/bin/env python3
# 0204.py
# matplot 을 이용한 grayscale 사진 출력 

import cv2
from matplotlib import pyplot as plt

imageFile = './data/lena.jpg'

imgGray = cv2.imread(imageFile, cv2.IMREAD_GRAYSCALE)

plt.axis('off')

plt.imshow(imgGray, cmap = "gray")

plt.show()

"""
plt.axis('off')
# 보간법 적용 하여 출력
# interpolation (보간법) = bicubic
plt.imshow(imgGray, cmap = "gray", interpolation = "bicubic")
plt.show()
"""
