# 0204.py
# matplot 을 이용한 grayscale 사진 출력 

import cv2
from matplotlib import pyplot as plt

imageFile = './data/lena.jpg'

imgGray = cv2.imread(imageFile, cv2.IMREAD_GRAYSCALE)

plt.axis('off')

plt.imshow(imgGray, cmap = "gray") #cmap (color map) = gray , interpolation (보간법 = 두점사이의 거리) = bicubic
plt.show()

"""
plt.axis('off')
plt.imshow(imgGray, cmap = "gray", interpolation = "bicubic") #interpolation = 보간법 설명 문서1
plt.show()
"""
