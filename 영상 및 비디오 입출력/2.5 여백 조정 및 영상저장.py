#0205.py
#여백 조정 및 영상 저장

import cv2
from matplotlib import pyplot as plt

imageFile='./data/lena.jpg'
imgGray = cv2.imread(imageFile,cv2.IMREAD_GRAYSCALE)

plt.figure(figsize =(6,6)) # figure  create ,출력 화면 크기설정
plt.subplots_adjust(left=0, right =1, bottom=0, top=1) #figure 좌표 설정
# left < right, bottom < top

plt.imshow(imgGray, cmap = 'gray') #current figure draw

#plt.axis('tight') # 그림을 모두 표시할만큼만의 크기로 설정

plt.axis('off') #x ,y 좌표 표시 x
plt.savefig('./data/0205.png') #cv2.write와 같다 current figure 저장
plt.show()
