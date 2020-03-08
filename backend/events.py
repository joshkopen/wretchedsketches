## List of events that we will listen to.
from flask_socketio import SocketIO

@socketio.on('room_connect')
def room_connect(sid, data):
	#data is a dict containing the room name and the displayname of the user
	

@socketio.on('drawing_submission')
def drawing_submit(sid, drawing_data):

@socketio.on('name_submission')
def name_submit(sid, name):




