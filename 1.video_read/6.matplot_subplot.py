#!/usr/bin/env python3
#0206.py

import cv2
from matplotlib import pyplot as plt

#데이터 경로 변수 설정
path = './data/'
imgBGR1 = cv2.imread(path + 'young.jfif')
imgBGR3 = cv2.imread(path + 'apple.jpg')
imgBGR2 = cv2.imread(path + 'baboon.jpg')
imgBGR4 = cv2.imread(path + 'orange.jpg')

#컬러 변환 : BGR -> RGB

imgRGB1 = cv2.cvtColor(imgBGR1 , cv2.COLOR_BGR2RGB)
imgRGB2 = cv2.cvtColor(imgBGR2 , cv2.COLOR_BGR2RGB)
imgRGB3 = cv2.cvtColor(imgBGR3 , cv2.COLOR_BGR2RGB)
imgRGB4 = cv2.cvtColor(imgBGR4 , cv2.COLOR_BGR2RGB)

#add a subplot to the current figure
# (2,2)의 서브플롯, figsize: 출력할 서브플롯의 크기, sharex, sharey 설정
#sharex , sharey  True 일씨 원래 사진크기로 맞춰짐
flg, ax = plt.subplots(2,2, figsize = (5,5),sharex =True, sharey = True)
#출력될 화면의 이름을 'Sample Pictures' 로 저장
#ax.ca~ 로 써도 상관없음
flg.canvas.set_window_title('Sample Pictures')


#aspect=auto -> 출력된 plot 창의 크기를 변경하여도 사진이 깨지지 않는다
ax[0][0].axis('off')
ax[0][0].imshow(imgRGB1,aspect = 'auto')

ax[0][1].axis('off')
ax[0][1].imshow(imgRGB2,aspect = 'auto')

ax[1][0].axis('off')
ax[1][0].imshow(imgRGB3,aspect = 'auto')

ax[1][1].axis('off')
ax[1][1].imshow(imgRGB4,aspect = 'auto')

# subplot 하나의 크기를 설정한다.
# 총 2,2 4개의 subplot을 가지며 left right bottom top 등을 이용하여 조정한다
# 이값들은 cm mm inch 와 같은 절대적인 크기가 아니라 상대적인 배율이다
# 0 ~ 1이 subplot을 선언할때 정했던figsize의 정 배율이며
# 이를 0~1 사이의 값으로 축소해서 출력하거나
# right나 top값을 1 이상으로 해서 확대해서 볼 수 있다
plt.subplots_adjust(left=0, bottom=0, right=0.5, top=1, wspace=0.5, hspace = 0.5) # 가로 , 세로 여백 0.05

# 사진 저장
plt.savefig("./data/0206.png", bbox_inches = 'tight')
plt.show()
