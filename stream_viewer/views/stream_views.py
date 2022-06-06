from flask import Blueprint, render_template, request, url_for, Response
from werkzeug.utils import redirect
import zmq
import base64
import cv2
import numpy as np

bp = Blueprint('stream', __name__, url_prefix='/stream')

host = '192.168.0.27'
# host = '127.0.0.1'
port = 5555
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect(f'tcp://{host}:{port}')
socket.setsockopt_string(zmq.SUBSCRIBE, np.unicode(''))


@bp.route('/play/')
def play():
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')
    
def gen():

    while True:
      stream = streamer()
      yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + stream + b'\r\n\r\n')

def streamer():
            
    while True:        
        frame = socket.recv_string()
        img = base64.b64decode(frame)
        npimg = np.fromstring(img, dtype=np.uint8)
        source = cv2.imdecode(npimg, 1)
        return cv2.imencode('.jpg', source)[1].tobytes()