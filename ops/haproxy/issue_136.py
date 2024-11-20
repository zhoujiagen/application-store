import socket, struct, time

for i in range(1000):
    print(i)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(("192.168.3.181", 8889))
        s.sendall(b'POST / HTTP/1.1\r\nHost: asdf\r\nContent-Length: 1000000\r\nConnection: keep-alive\r\n\r\n' + bytes(1000000*'a', 'ascii'))
        s.close()