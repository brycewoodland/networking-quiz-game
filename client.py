import socket

def start_client():
    c = socket.socket()
    c.connect(('localhost', 9999))

    while True:
        question = c.recv(1024).decode('utf-8')
        if not question:
            break
        print(question)
        answer = input("Your answer: ")
        c.send(answer.encode('utf-8'))
        result = c.recv(1024).decode('utf-8')
        print(result)

    c.close()

if __name__ == "__main__":
    start_client()