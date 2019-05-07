# 0201.py
"""
사용하는 함수

imread(filename[,flags]) filename의 영상파일을 numpy.ndarray의 배열로 읽어 반환 읽기에 실패시 None 반환

imwrite(filename,img[,params]) numpy.ndarry의 배열 img를  filename의 영상파일로 저장 , 파일의 확장자에 의해 영상 포맷이 결정

namedWindow(winname[,flags]) winname 이름을 갖는 윈도우를 생성

imshow(winname, mat) winname 윈도우에 영상 mat를 표시함 winname윈도우가 없으면 생성

waitKey([,delay]) 키보드 입력을 위해 delay (ms) 만큼 대기, delay = 0 이면 키보드 입력이 있을때 까지 무한대기 , 지정된 시간안에 키가 입력되지 않으면 -1 return

destroyAllWindows() 모든 윈도우 파괴
destroyWindow()     주어진 윈도우만 파괴
"""
import cv2

imageFile = './data/lena.jpg'
img = cv2.imread(imageFile) # if(flag== default) => color
img2 = cv2.imread(imageFile,0) #if(flag==0) => grayscale

cv2.imshow('Lena color',img)    #img 사진 출력
cv2.imshow('Lena grayscale',img2)   #img2 사진 출력

cv2.waitKey()   #키대기
cv2.destroyAllWindows() #종료
