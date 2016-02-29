from socketIO_client import SocketIO, LoggingNamespace

def on_response(*args):
    print('Response from Bang server: ' + args[0])
with SocketIO('localhost', 5000, LoggingNamespace) as socketIO:
    socketIO.emit('hoang sida', {'message': 'Lieu hoang co bi benh sida ? '}, on_response)
    socketIO.wait_for_callbacks(seconds=1)
