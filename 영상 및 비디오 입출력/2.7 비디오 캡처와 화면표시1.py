# 0207.py
import cv2

#카메라이용
##cap = cv2.VideoCapture(0)  # 0번 카메라

#video 영상이용
cap = cv2.VideoCapture('./data/vtest.avi')


#카메라 이용시 frame size 조절
##cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
##cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)


#cap.get  비디오 프레임의 가로 세로 크기 속성을 읽어 정수로 변환 후
           #frame size에 할당

frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
              int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('frame_size =', frame_size)


#무한반복루프

while True:   
    retval, frame = cap.read() # 프레임 캡처
    if not retval:
        break

    cv2.imshow('frame',frame)
    
    key = cv2.waitKey(25)
    if key == 27: # Esc
        break
if cap.isOpened(): #객체가 열려있다면 닫고 윈도우 창 종
    cap.release()
cv2.destroyAllWindows()
