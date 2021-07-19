import socket

HOST = '127.0.0.1'
PORT = 65432

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
with s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    print(conn)
    print(addr)
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if (not data):
                break
            conn.sendall(data)
        #print(data)
#print("Hello World")