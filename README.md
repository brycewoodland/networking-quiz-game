## Overview

**Project Title**: Networking Quiz Game

**Project Description**: A quiz game that uses networking capabilities to connect clients and a server. 
Players can join the game, answer quiz questions, and receive feedback on their answers in real-time.

**Project Goals**:
- Create an interactive quiz game that can support multiple players.
- Implement server-client architecture to facilitate communication.
- Provide real-time feedback on answers and track scores.

## Instructions for Build and Use

Steps to build and/or run the software:

1. Ensure you have Python installed (version 3.6 or higher recommended)
2. Start the server by running:
   ```bash
   python server.py
   ```
4. Connect clients by running the client code in a separate terminal:
   ```bash
   python client.py
   ```

Instructions for using the software:

1. When prompted in the client terminal, enter your name to join the game.
2. Answer the quiz questions as they appear on your screen.
3. At the end of the quiz, your final score will be displayed.

## Development Environment 

To recreate the development environment, you need the following software and/or libraries with the specified versions:

* Python (version 3.6 or higher)
* Threading library (included with Python standard library)
* Socket Library (included with Python standard library)

## Useful Websites to Learn More

I found these websites useful in developing this software:

* [Socket Programming Using Python](https://www.youtube.com/watch?v=u4kr7EFxAKk)
* [Python Socket Programming Tutorial](https://www.youtube.com/watch?v=3QiPPX-KeSc)
* [socket - Low-level networking interface](https://docs.python.org/3.6/library/socket.html)
* [Socket Programming HOWTO](https://docs.python.org/3/howto/sockets.html)
* [An Intro to Threading in Python](https://realpython.com/intro-to-python-threading/)

## Future Work

The following items I plan to fix, improve, and/or add to this project in the future:

* [ ] Implement a GUI for a more user-friendly interface.
* [ ] Add more quiz questions and categories. Allow users the ability to submit quiz questions.
* [ ] Enhance error handling to gracefully disconnect clients from the server.
