import socketio

sio = socketio.Client()

@sio.event
def connect():
    print('connection established')

@sio.on('mouse')
def my_message(data):
    print('message received with ', data)
    sio.emit('my response', {'response': 'my response'})

@sio.event
def disconnect():
    print('disconnected from server')

sio.connect('http://localhost:3001')
sio.wait()
