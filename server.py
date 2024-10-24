import socket

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

def start_server():
    s = socket.socket()
    print('Socket Created')
    s.bind(('localhost', 9999))
    s.listen(3)
    print('Waiting for connections')

    while True:
        c, addr = s.accept()
        print("Connected with ", addr)

        for question, options, answer in quiz:
            question_with_options = (
                f"{question}\nOptions:\n" + 
                "\n".join([f"{i+1}. {option}" for i, option in enumerate(options)])
            )
            c.send(question_with_options.encode('utf-8'))
            client_answer = c.recv(1024).decode('utf-8')
            if client_answer.lower() == answer.lower():
                c.send('Correct!\n'.encode('utf-8'))
            else:
                c.send('Incorrect!\n'.encode('utf-8'))

        c.close()

if __name__ == "__main__":
    start_server()