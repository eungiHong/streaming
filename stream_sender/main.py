import os
import argparse

from utils.socket.pub import Publisher
from utils.video.streamer import Streamer


def run(src, port):

    streamer = Streamer(src)
    publisher = Publisher(port)

    while True:
        frame = streamer.play()
        publisher.publish(frame)



if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--src', type=str, help='path to the video source')
    parser.add_argument('--port', type=str, help='port number')
    
    opt = parser.parse_args()

    run(opt.src, opt.port)