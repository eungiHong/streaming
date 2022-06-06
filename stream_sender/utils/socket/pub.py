import zmq


class Publisher:

    def __init__(self, port):

        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PUB)
        self.socket.bind(f'tcp://*:{port}')
    
    def publish(self, data):
                        
        if data is not None:            
            self.socket.send(data)