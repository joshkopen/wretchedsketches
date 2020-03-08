from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

if __name__ == '__main__':
    socketio.run(app)

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)

@socketio.on('testEvent')
def handle_test_event(arg1, arg2, arg3):
    print('received args: ' + arg1 + arg2 + arg3)

def present(sequences, players):
    for i in sequences:
        sequences[i].display(players[i])
        #wait for socket for next player's button press "start sequence" 
        #socket blackbox1
        #at the end wait for the 'end round' button
        #socket blackbox2

def display(input):
    text = (input[0] == 'i')
    if(input is text):
        #send text to socket
        #socket blackbox3
        #wait for next from socket
        #socket blackbox4
    else:
        #send image to socket
        #socket blackbox5
        #wait for next from socket
        #socket blackbox4
