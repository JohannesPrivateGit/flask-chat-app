# Flask Chat App
A simple chat app built with Flask and SocketIO.

. . .

This code is from a software project for CHAMÄLEON Stralsund e.V.
Besides providing a reliable chat service for the company, it also serves as a game including roles with respective profile pictures and 
role descriptions. 
The purpose of the game is to teach teenagers about the possible dangers of chatting with strangers on the internet.

## Setting Up the Project
### 1. Clone the Project
Clone the project to a location on your device and make sure that Python 3 is installed.
### 2. Install Python Librarys
Run the following commands in your terminal:
```
pip install flask
pip install flask_socketio
```
### 3. Choose a save App Password
Open app.py and go to line 6. It should look like this:
```
APP_PASSWORD = "1223"
```
Enter your personal password into the quotation marks.
### 4. Run the App
To run the app, execute the following command in your terminal:
```
flask run
```
Then go into your browser and type in the following URL:
```
http://127.0.0.1:5000/
```
