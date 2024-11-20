# TCP Echo Server

## Python Version

Session 1:
```shell
$ python main.py localhost 8000
waiting for a connection
Connected by ('127.0.0.1', 55766)
waiting for a connection
Connected by ('127.0.0.1', 55768)
$
```

Session 2:
```shell
$ telnet localhost 8000

localhost:8000 > aaa
hello
localhost:8000 > hello
exit

Connection to host lost.


$ telnet localhost 8000

localhost:8000 > aaa
DESTROY

Connection to host lost.
```