# RabbitMQ

- https://www.rabbitmq.com/
- https://hub.docker.com/_/rabbitmq

Access `http://localhost:15672/` with `devops/devops+rabbitmq`.

## Clients

### Python

- https://pika.readthedocs.io/

```shell
# Windows WSL
$ python --version
Python 3.11.5
$ python -m virtualenv .venv
$ source .venv/Scripts/activate
$ pip install kafka-python
$ pip freeze > requirements.txt
```

```
# create queue 'test' on vhost '/'
# create exchange 'test' on vhost '/' with binding to queue 'test' with routing key 'test'
```

```shell
$ python blocking_publisher.py
$ python blocking_consumer.py
<Basic.Deliver(['consumer_tag=ctag1.c473866f4e134ff8b8e1a165edc9850f', 'delivery_tag=1', 'exchange=test', 'redelivered=True', 'routing_key=test'])> <BasicProperties> b'Test message.'
```