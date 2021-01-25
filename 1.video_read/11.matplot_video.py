#!/usr/bin/env python3
# 0211.py
import cv2
import matplotlib.pyplot as plt

#1 esc 를 누르면 객체를 해제하고 출력 창을 닫는다
# mpl_connect 제어 함수
def handle_key_press(event):
    if event.key == 'escape':
        cap.release()
        plt.close()       
def handle_close(evt):
    print('Close figure!')
    cap.release()

#2 프로그램 시작    
cap = cv2.VideoCapture(0) # 0번 카메라

plt.ion() # 대화모드 설정
fig = plt.figure(figsize=(10, 6)) # fig.set_size_inches(10, 6)
plt.axis('off')
#ax = fig.gca()
#ax.set_axis_off()
fig.canvas.set_window_title('Video Capture')

#윈도우 닫기 이벤트를 처리할 함수 설정
#mpl_connect ('정해진 제어 문자열(string), 그에 따라 사용할 함수명)
#key_press_event = 이벤트키가 눌렸을때 handle_key_press 함수 호출
#close_event = figure 가 닫혔을때 발생하는 이벤트
fig.canvas.mpl_connect('key_press_event', handle_key_press)
fig.canvas.mpl_connect('close_event', handle_close)


#첫 프레임 캡처는 항상 필요하다
retval, frame = cap.read() 
# im AxesImage 영상이다
im = plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

#3
while True:
    retval, frame = cap.read() # 프레임 캡처 
    if not retval:
        break       
#    plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    #AxesImage 로 변경 (imshow로 변경하는 것 보다 빠르다)
    #캡처된 프레임을 rgb로 변경
    im.set_array(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    #캔버스 그리기
    fig.canvas.draw()
    
    #GUI 이벤트 루프로 돌아가면 위젯다시그리기를 요청한다
    #fig.canvas.draw_idle()
    
    #flush_events()를 이용하여 다른 사용자 인터페이스(GUI)를 처리할 수 있다
    fig.canvas.flush_events()  # plt.pause(0.001)
if cap.isOpened():
    cap.release()
