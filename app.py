# This file will have all Flask related code.

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_socketio import SocketIO, join_room

APP_PASSWORD = "1223"


# Initializing Flask.
app = Flask(__name__)

# Initializing SocketIO.
socketio = SocketIO(app)

# Global variables.
USER_LIST = []

# Renders login page.
@app.route('/')
def home():
    return render_template("index.html")


# Renders chat page.
@app.route('/chat')
def chat():
    # Gets username and chatroom from previous webpage.
    username = request.args.get('username')
    room = request.args.get('room')
    password = request.args.get('password')

    # Check if user entered thee right password.
    if password != APP_PASSWORD:
        return redirect(url_for('home'))

    # Only add new user to the list if it is not a spectator.
    if username == "spectator":
        pass
    else:
        # Adds new username to users list.
        USER_LIST.append(username)
        print(USER_LIST)

    # Checks if there has been valid inputs.
    if username and room:
        # To make sure, that user names are not printed twice by html
        # and sockets, only return user list without the last entry.
        user_list_without_last_user = USER_LIST[:-1]

        return render_template('chat.html',
                               username=username,
                               room=room,
                               user_list=user_list_without_last_user,
                               role=str.lower(username))
    
    # If not, redirect to home page and let user type in data again.
    else:
        return redirect(url_for('home'))


# Handles event that user sends a message in a room.
@socketio.on('send_message')
def handle_send_message_event(data):
    # Prints out a message in the Flask Terminal.
    app.logger.info("{} has send a message to the room {}: {}".format(
        data['username'], data['room'], data['message'])
    )

    socketio.emit('receive_message', data, room=data['room'])


# Handles event that user joins a room.
@socketio.on('join_room')
def handle_join_room_event(data):
    # Prints out a message in the Flask Terminal.
    app.logger.info("{} has joined the room {}".format(
        data['username'], data['room'])
    )
    
    join_room(data['room'])
    
    socketio.emit('join_room_announcement', data)


# Python main function runs SocketIO which includes the Flask app.
if __name__ == '__main__':
    socketio.run(app, debug=False, host='0.0.0.0')
