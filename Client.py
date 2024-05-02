import socket
import threading

# global client_name
def connect_to_server():
    client_name = input("Enter your name: ")
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 8080))
    print("Connected to server.")

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,client_name))
    receive_thread.start()

    while True:
        message = input("You : ")
        dest = input("To : ")
        with open("myfile.txt", "w") as f:
            f.write(dest)
        send_message(client_name + ": " + message, client_socket)

def receive_messages(client_socket,client_name):
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        with open("myfile.txt", 'r') as f:
            content = f.read()
        # print(client_name)
        # if client_name==dest : print message
        if client_name == content:
            print(message)

def send_message(message, client_socket):
    client_socket.send(message.encode('utf-8'))

if __name__ == "__main__":
    connect_to_server()
