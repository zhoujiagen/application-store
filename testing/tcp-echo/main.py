# socket — Low-level networking interface
# https://docs.python.org/3/library/socket.html

import socket
import sys
import threading


def handler(connection, client_address):
    with connection:
        print('Connected by', client_address)
        all_data = bytes()
        while True:
            data = connection.recv(1024)
            if not data:
                print("NO DATA", flush=True)
                break
            all_data = all_data + data
            print(all_data, flush=True)

            if all_data.endswith(b'\n') or all_data.endswith(b'\r\n'):
                connection.sendall(
                    bytes(f"{host}:{port} > ", "utf-8") + all_data)
                all_data = bytes()
            elif all_data.endswith(bytes("exit", "utf-8")):
                break
        print('Finish', client_address, flush=True)
        return client_address


if __name__ == '__main__':
    host = sys.argv[1]
    port = int(sys.argv[2])
    server_address = ((host), (port))

    handlers = []
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(server_address)
        sock.listen(32)
        while True:
            try:
                print('waiting for a connection', flush=True)
                connection, client_address = sock.accept()
                t = threading.Thread(target=handler, args=(
                    connection, client_address))
                handlers.append(t)
                t.start()
            except KeyboardInterrupt:
                print("QUIT", flush=True)
                break

        print("Bye!", [t.join() for t in handlers], flush=True)
