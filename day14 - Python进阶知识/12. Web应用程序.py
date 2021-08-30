# 同源策略
# 协议 & 域名 & 端口
# Error: Access-Control-Allow-Origin

import socket
import json

sk = socket.socket()
sk.bind(('127.0.0.1', 2021))
sk.listen()

while True:
    print('Server is running......')
    conn, addr = sk.accept()
    recv_data = conn.recv(1024)
    print('recv_data:', recv_data.decode())
    stocks = [
        {'name': '中信证券', 'code': '600030', 'price': '24.73'},
        {'name': '格力电器', 'code': '000651', 'price': '41.27'},
        {'name': '双汇发展', 'code': '000895', 'price': '24.16'},
        {'name': '元组股份', 'code': '603886', 'price': '18.07'},
        {'name': '中国银行', 'code': '601988', 'price': '3.00'},
    ]
    data = json.dumps(stocks)
    conn.send(b'HTTP/1.1 200 OK\r\nAccess-Control-Allow-Origin: *\r\n\r\n'+data.encode())
    conn.close()