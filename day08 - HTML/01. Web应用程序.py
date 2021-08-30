import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 2021))
sk.listen()

while True:
    print('Server is running......')
    conn, addr = sk.accept()
    recv_data = conn.recv(1024)
    print('recv_data:', recv_data.decode())
    with open('index.html', 'rb') as f:
        data = f.read()
    conn.send(b'HTTP/1.1 200 OK\r\n\r\n'+data)
    conn.close()