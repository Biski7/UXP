import socket
import threading

PORT = 5050

SIZE = 1024
DISCONNECT_MESSAGE = '!END'
FORMAT = 'utf-8'
SERVER = '192.168.137.1'
# OR
SERVER = socket.gethostbyname(socket.gethostname())

ADDR = (SERVER, PORT)

def main():
    print("[STARTING] Server is starting...")
    # create socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print(f"[LISTENING] The server is listening on {SERVER}")
    connected = True
    while connected:
        conn, addr = server.accept()
        # print(conn.recvfrom(65565))
        mes = conn.recv(SIZE).decode(FORMAT)
        print(f'[CLIENT] {mes}')
        connected = False
        break

        # thread = threading.Thread(target = handle_client, args = (conn, addr))
        # thread.start()
        # print(f'[ACTIVE CONNECTIONS] {threading.activeCount() -1}')



# def handle_client(conn, addr):
#     print(f"[NEW CONNECTION] {addr} connected ")
#     connected2 =True

#     while connected2:
#         mes = conn.recv(SIZE).decode(FORMAT)
#         print(f'[CLIENT] {mes}')
#         connected2 = False
#         break
#         # if str(mes) == DISCONNECT_MESSAGE:
#         #     connected2 = False
#         #     break
#         # else:
#         #     inp = input('> ')
#         #     conn.send(inp.encode(FORMAT))

#     conn.close()


if __name__ == "__main__":
    main()

