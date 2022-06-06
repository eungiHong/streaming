import cv2
import numpy as np
import base64


class Streamer:

    def __init__(self, src):
        
        self.cap = cv2.VideoCapture(src)

        if self.cap.isOpened() is False:
            print(f'Video stream is not created. check the source configuration: {src}')

        
    def play(self):
                
        ret, frame = self.cap.read()

        if ret is False:
            # print('Failed to read a frame')
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 1)
            return None
        
        else:
            # data = np.frombuffer(frame, dtype=np.uint8).reshape(frame.shape)            
            # _, jpeg_data = cv2.imencode('.jpg', data)            
            # return jpeg_data

            # frame = cv2.resize(frame, (640, 480))
            encoded, buffer = cv2.imencode('.jpg', frame)
            jpg_as_text = base64.b64encode(buffer)
            return jpg_as_text
        