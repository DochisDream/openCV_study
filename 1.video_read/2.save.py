#!/usr/bin/env python3
# 0202.py
#imwrite(filename,img[,params]) numpy.ndarry의 배열 img를  filename의 영상파일로 저장 , 파일의 확장자에 의해 영상 포맷이 결정

import cv2

imageFile='./data/lena.jpg'
img = cv2.imread(imageFile) #color

#파일 확장자 변경하며 저장
cv2.imwrite('./data/lena.bmp', img)
cv2.imwrite('./data/lena.png', img)
cv2.imwrite('./data/lena2.png',img, [cv2.IMWRITE_PNG_COMPRESSION, 9])   #img를 압축률 9 PNG영상으로 저장 압축률이 높을수록 시간 오래걸림 , default =3
cv2.imwrite('./data/lena2.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 90])    #img를 90%의 품질을 갖는 JPEG영상으로 저장 품질의 범위는 [0,100] 높을수록 영상의 품질이 좋다 default =95

