# Voice Messenger — Python TCP Text & Voice Chat

A Python client–server application that supports sending text messages and recording/sending voice messages over TCP sockets.

---

## Instructions for Build and Use

### Steps to build and/or run the software:

1. Navigate to the project folder:
   ```bash
   cd ~/PycharmProjects/voice_messenger
Activate the virtual environment:
source .venv/bin/activate
- Run the server:
python3 server.py
- Open a second terminal and activate the environment again:
source .venv/bin/activate
- Run the client:
python3 client.py
### Instructions for Using the Software
Choose an option from the client menu:
1) Send Text
2) Record & Send Voice
3) Quit
Option 1: Sends a text message to the server.
Option 2: Records audio, sends it to the server, and the server stores it as a .wav file.
Option 3: Exits the client.
## Development Environment
### To recreate the development environment, you need:
Python 3.11+
Homebrew (macOS)
brew install portaudio
PyAudio
pip install pyaudio
Project dependencies
pip install -r requirements.txt
### Useful Websites to Learn More
- https://realpython.com/python-sockets/
- https://people.csail.mit.edu/hubert/pyaudio/
- https://docs.python.org/3/library/threading.html
- https://docs.python.org/3/library/wave.html
### Future Work
 - Add audio playback feature
 - Add usernames for clients
 - Add message history
 - Add encryption
 - Build a GUI
