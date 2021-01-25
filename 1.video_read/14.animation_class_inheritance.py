#!/usr/bin/env python3
# 0214.py

import cv2
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class   Video(animation.FuncAnimation):
    def __init__(self, device=0, fig = None, frames = None, interval = 100, repeat_delay = 5, blit = False, **kwargs):
        
        if fig is None:
            self.fig = plt.figure()
            self.fig.canvas.set_window_title('Video Capture')
            plt.axis("off")
        
        # animation.FuncAnimation 의 init (생성자)를 가져와서 class 를 가져와서 사용한다
        # 자식클래스인 video 에서 init을 overiding 했기 때문에 부모클래스인 animatin.FuncAnimation 의 init(생성자)를 다시 가져와서 값을 설정해준다
        super(Video, self).__init__(self.fig, self.updateFrame, init_func = self.init, frames = frames, interval = interval, blit = blit, repeat_delay = repeat_delay, **kwargs)
        self.cap = cv2.VideoCapture(device)
        print("start capture ...")


    def init(self):
        retval, self.frame = self.cap.read()
        if retval:
            self.im = plt.imshow(cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB))

    def updateFrame(self, k):
        retval, self.frame = self.cap.read()
        if retval:
            self.im.set_array(cv2.cvtColor(camera.frame, cv2.COLOR_BGR2RGB))
            #return self.im
    def close(self):
        if self.cap.isOpened():
            self.cap.release()
        print("finish capture.")

# 프로그램 시작

#camera = Video()
camera = Video('./data/vtest.avi')
plt.show()
camera.close()
