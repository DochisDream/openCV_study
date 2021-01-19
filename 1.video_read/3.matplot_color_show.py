#!/usr/bin/env python3
# 0203.py
# matplot을 이용한 img 출력
# openCV는 img를 BGR로 처리하고, matplotlib 는 RGB 순서로 처리하기 때문에 항상 BGR - > RGB 변환 해줘야 제대로된 img가 출력된다

import cv2
# matplotlib 에서 pyplot 을 사용하는데 plt라는 변수로 사용
from matplotlib import pyplot as plt

imageFile='./data/lena.jpg'
imgBGR = cv2.imread(imageFile) #cv2.IMREAD_COLOR

# X, Y축을 표시하지 않는다
# 화면을 출력할 때마다 해줘야 적용된다
plt.axis('off')

#BGR로 img출력
plt.imshow(imgBGR)
plt.show()


imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)  #BGR -> RGB변환
#plt.axis('off')   화면을 출력할 때마다 해줘야 적용된다
plt.imshow(imgRGB)
plt.show()
