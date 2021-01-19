# 0209.py
'''
 pip install youtube_dl
 pip install pafy
'''
import cv2, pafy
url = 'https://www.youtube.com/watch?v=u_Q7Dkl7AIk'
video = pafy.new(url)
print('title = ', video.title) #영상제목
print('video.rating = ', video.rating) 
print('video.duration = ', video.duration) #영상길이

best = video.getbest(preftype='webm')     # 'mp4','3gp' 객체 best를 생성
print('best.resolution', best.resolution) #비디오 해상도 출력

cap=cv2.VideoCapture(best.url) #url을 이용하여 cap객체를 생성
while(True):
        retval, frame = cap.read()
        if not retval:
                break
        cv2.imshow('frame',frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray,100,200) #canny 알고리즘을 사용하여 edge를 찾는다
        cv2.imshow('edges',edges)

        key = cv2.waitKey(25)
        if key == 27: # Esc
                break 
cv2.destroyAllWindows()
