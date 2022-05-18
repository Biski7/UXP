import socket

from sqlalchemy import false

IP = socket.gethostbyname(socket.gethostname())
# print(IP)
# IP = '192.168.1.131'
PORT = 5050
DISCONNECT_MESSAGE = '!END'
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024

def main():
    connected = True
    """ Staring a TCP socket. """
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    """ Connecting to the server. """
    client.connect(ADDR)

    # """ Opening and reading the file data. """
    # # file = open("data/sample.uxp", "r")
    # file = open("data/myData.txt", "r")
    # data = file.read()

    # """ Sending the filename to the server. """
    # # client.send('sample.uxp'.encode(FORMAT))
    # client.send('myData.txt'.encode(FORMAT))

    # msg = client.recv(SIZE).decode(FORMAT)
    # print(f"[SERVER]: {msg}")

    # """ Sending the file data to the server. """
    # client.send(data.encode(FORMAT))
    # msg = client.recv(SIZE).decode(FORMAT)
    # print(f"[SERVER]: {msg}")

    # """ Closing the file. """
    # file.close()

    while connected:
        u_inp = 'a'*1000
        client.send(u_inp.encode(FORMAT))
        connected = False
        break


    """ Closing the connection from the server. """
    client.close()


if __name__ == "__main__":
    main()