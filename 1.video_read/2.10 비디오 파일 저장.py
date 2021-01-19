# 0210.py
import cv2

cap = cv2.VideoCapture(0) # 0번 카메라
frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
              int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('frame_size =', frame_size)

#fourcc = cv2.VideoWriter_fourcc(*'DIVX')  # ('D', 'I', 'V', 'X')
fourcc = cv2.VideoWriter_fourcc(*'XVID') #코덱 4- 문자로 설정

# Video.Writer객체 생성  저장위치 및 이름  설정한코덱  fps    화면 크기   isColor=False => gray
out1 = cv2.VideoWriter('./data/record0.mp4',fourcc, 5.0, frame_size)
out2 = cv2.VideoWriter('./data/record1.mp4',fourcc, 5.0, frame_size,isColor=False)

while True:
    retval, frame = cap.read() #프레임을 카메라로 부터 읽어옴
    if not retval:
        break   
    out1.write(frame) #프레임 저장
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out2.write(gray)        
    cv2.imshow('frame',frame) #프레임 출력
    cv2.imshow('gray',gray)      
    
    key = cv2.waitKey(25)
    if key == 27:
        break
cap.release()
out1.release()
out2.release()
cv2.destroyAllWindows()
