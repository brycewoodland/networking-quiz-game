import socket

def start_client():
    # Create a socket object
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to server running localhost at port 9999
    c.connect(('localhost', 9999))

    name = input("Enter your name: ")
    c.send(name.encode('utf-8'))
    quiz_active = True
    try:
        while quiz_active:
            # Recieve a question from the server
            question = c.recv(1024).decode('utf-8')
            if question.startswith('Quiz over!'):
                print(question)
                quiz_active = False
            else:
                print(question)
                answer = input("Your answer: ")

                # Send the client's answer to the server
                c.send(answer.encode('utf-8'))

                # Recieve the result (Correct/Incorrect) from the server
                result = c.recv(1024).decode('utf-8')
                print(result)
    
    except ConnectionResetError:
        print('Connection to server lost.')
    finally:
        # Close the connection to the server
        c.close()

if __name__ == "__main__":
    start_client()