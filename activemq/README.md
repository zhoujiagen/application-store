# ActimveMQ Artemis

- https://activemq.apache.org/components/artemis/documentation/
- Python stomp.py: https://jasonrbriggs.github.io/stomp.py/quickstart.html

Access `http://localhost:18161/` with `devops/devops+artemis`/

```shell
# stomp.py
$ python --version                                                                   in cmd at 23:25:23
Python 3.11.5
$ python -m virtualenv .venv
$ source .venv/Scripts/activate
.venv $ .venv/Scripts/pip install stomp.py

.venv $ .venv/Scripts/stomp.exe --version
8.1.0
.venv $ stomp -H localhost -P 61613 -U devops -W devops+artemis

> subscribe /queue/test
Subscribing to '/queue/test' with acknowledge set to 'auto', id set to '1'
> send /queue/test hello world
>
message-id: 40
subscription: 1

hello world
>
```