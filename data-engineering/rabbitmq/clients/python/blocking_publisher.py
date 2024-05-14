import pika

if __name__=="__main__":
  parameters = pika.ConnectionParameters(
    host="localhost",
    credentials=pika.PlainCredentials(username="devops", password="devops+rabbitmq"))
  with pika.BlockingConnection(parameters=parameters) as conn:
    channel = conn.channel()
    channel.basic_publish(exchange='test', routing_key='test',
                          body=b'Test message.')