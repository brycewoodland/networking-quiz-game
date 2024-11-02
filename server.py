import socket
import threading

quiz = [
    ('What is the atomic number of oxygen?', 
     ['6', '7', '12', '8'], '8'),
    ('Which planet is the hottest in our solar system?', 
     ['Pluto', 'Venus', 'Saturn', 'Mercury'], 'Venus'),
    ('What is the rarest blood type in humans?', 
     ['AB', 'O', 'A', 'B'], 'AB'),
    ('What is the most abundant gas in Earth\'s atmosphere', 
     ['oxygen', 'carbon', 'nitrogen', 'fluorine'], 'nitrogen'),
    ('Who developed the theory of general relativity?', 
     ['Isaac Newton', 'Albert Einstein', 'Galileo Galilei', 
      'Nikola Tesla'], 'Albert Einstein'),
    ('Which element has the chemical symbol \'Fe\'?', 
     ['Iron', 'Fluorine', 'Francium', 'Fermium'], 'iron'),
    ('What is the powerhouse of the cell?', 
     ['Mitochondria', 'Nucleus', 'Ribosome', 'Chloroplast'], 
     'mitochondria'),
    ('How many bones are there in the adult human body?', 
     ['204', '205', '206', '207'], '206'),
    ('Which planet has the most moons?', 
     ['Earth', 'Mars', 'Saturn', 'Jupiter'], 'Jupiter'),
    ('What is the name of the first artificial satellite to orbit Earth?', 
     ['Explorer 1', 'Sputnik 1', 'Vanguard 1', 'Luna 1'], 'Sputnik 1')
]

clients = []
scores = {}

def handle_client(client_socket, client_address):
    client_name = client_socket.recv(1024).decode('utf-8')
    print(f'{client_name} from {client_address} has joined the game.')
    clients.append(client_socket)
    scores[client_socket] = 0

    # Iterate through each quiz question
    for question, options, correct_answer in quiz:
        # Format the question with its options
        question_message = (f"{question}\nOptions:\n" + 
            "\n".join([f"{i+1}. {option}" for i, option in enumerate(options)])
        )

        # Send the question to the client
        client_socket.send(question_message.encode('utf-8'))
            
        try:
            # Receive and check each client's answer
            client_response = client_socket.recv(1024).decode('utf-8')
            # Check if the answer is correct or incorrect
            if client_response.lower() == correct_answer.lower():
                client_socket.send('Correct!\n'.encode('utf-8'))
                scores[client_socket] += 1
            else:
                client_socket.send('Incorrect!\n'.encode('utf-8'))
        except ConnectionResetError:
            print(f'{client_name} from {client_address} disconnected.')
            break

    # End of game summary
    client_socket.send('Quiz over!\n'.encode('utf-8'))
    score_message = f'{client_name}, your final score is {scores[client_socket]}.\n'
    client_socket.send(score_message.encode('utf-8'))

    # Close the connection
    client_socket.close()
    clients.remove(client_socket)
    print(f'{client_name} has left the game.')


def start_server():
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket Created')
    s.bind(('localhost', 9999)) # Bind the socket to localhost on port 9999
    s.listen(5) # listen for incoming connections (up to 5 clients in queue)
    print('Quiz game server started, waiting for players...')

    while True:
        # Accept a connection from client
        client_socket, client_address = s.accept()

        # Create a new thread for each client connection
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == "__main__":
    start_server()