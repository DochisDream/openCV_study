#!/usr/bin/env python3
# 0212.py

import cv2
import matplotlib.pyplot as plt

# matplotlib.animation을 animation으로 임포트하여 애니메이션으로 비디오를 처리한다.
import matplotlib.animation as animation

''' 카메라 대신 youtube 영상대체
import pafy
url = 'https://www.youtube.com/watch?v=u_Q7Dkl7AIk'
video = pafy.new(url)
print('title = ', video.title)
print('video.rating = ', video.rating)
print('video.duration = ', video.duration)

best = video.getbest(preftype='mp4')     # 'webm','3gp'
print('best.resolution', best.resolution)

cap=cv2.VideoCapture(best.url)
'''

#프로그램 시작
# video 객체 생성
cap = cv2.VideoCapture(0)

#figure 객체 사이즈 설정
fig = plt.figure(figsize = (10, 6)) #fig.set_size_inches(10,6)

# 타이틀
fig.canvas.set_window_title('Video Capture')

#축 표현 제거
plt.axis('off')

#애니메이션에서 초기화를 위해 한번 호출할 함수 init()을 정의
def init():
    #전역변수가 아니라면 첫프레임 캡쳐가 안되기 때문에 정상적인 프로그램 동작 불가
    global im

    retval, frame = cap.read() #첫 프레임 캡처
    im = plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)) # imshow를 이용한 색상 공간 변환
    #return im


# 매개변수 인수 k는 애니메이션 프레임 번호 0,1,2 등이 전달된다.
def updateFrame(k):
    retval, frame = cap.read()
    if retval:
        im.set_array(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

#animation 설정
# fig에서 , 갱신함수 updateFrame(), 초기화 함수 init(), 프레임 간격을 50밀리초로 애니메이션 설정
# 컴퓨터 성능이 안좋으면 비디오가 멈추기 때문에 interval 간격을 조절할것
ani = animation.FuncAnimation(fig, updateFrame, init_func = init, interval = 100)

#animation이 끝날때까지 plt.show
plt.show()

    #객체가 열려 있다면 객체 해제
if cap.isOpend():
    cap.release()
