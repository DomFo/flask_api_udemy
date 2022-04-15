#Modified by smartbuilds.io
#Date: 27.09.20
#Desc: This scrtipt script..

import cv2
from imutils.video.pivideostream import PiVideoStream
import imutils
import time
from datetime import datetime
import numpy as np

from PIL import Image
from pycoral.adapters import classify
from pycoral.adapters import common
from pycoral.utils.dataset import read_label_file
from pycoral.utils.edgetpu import make_interpreter

face_cascade = cv2.CascadeClassifier('assets/models/haarcascade_frontalface_default.xml')


class VideoCamera(object):
    def __init__(self, flip = False):
        self.vs = PiVideoStream().start()
        self.flip = flip
        self.last_frame = datetime.now()
        time.sleep(2.0)

    labels = read_label_file(labels) if args.labels else {}

    interpreter = make_interpreter(*args.model.split('@'))
    interpreter.allocate_tensors()


    def __del__(self):
        self.vs.stop()

    def flip_if_needed(self, frame):
        if self.flip:
            return np.flip(frame, 0)
        return frame

    def put_face(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        # Draw the rectangle around each face
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        return frame


    def put_timestamp(self, frame):
        font = cv2.FONT_HERSHEY_PLAIN
        cv2.putText(frame, str(datetime.now().time()), (20, 40),
                    font, 2, (255, 255, 255), 2, cv2.LINE_AA)
        return frame

    def put_fps(self, frame):
        font = cv2.FONT_HERSHEY_PLAIN
        delta_t = datetime.now() - self.last_frame
        fps = (1 / delta_t.microseconds) * 10E5
        cv2.putText(frame, f'FPS: {fps:.1f}', (20, 40),
                    font, 2, (255, 255, 255), 2, cv2.LINE_AA)
        self.last_frame = datetime.now()
        return frame

    def get_frame(self):
        frame = self.flip_if_needed(self.vs.read())
        frame = self.put_face(frame)
        frame = self.put_fps(frame)
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()