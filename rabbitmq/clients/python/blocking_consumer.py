import pika

if __name__=="__main__":
  parameters = pika.ConnectionParameters(
    host="localhost",
    credentials=pika.PlainCredentials(username="devops", password="devops+rabbitmq"))
  with pika.BlockingConnection(parameters=parameters) as conn:
    channel = conn.channel()

    for method_frame, properties, body in channel.consume('test'):
        # Display the message parts and acknowledge the message
        print(method_frame, properties, body)
        channel.basic_ack(method_frame.delivery_tag)

        # Escape out of the loop after 10 messages
        if method_frame.delivery_tag == 10:
            break

    # Cancel the consumer and return any pending messages
    requeued_messages = channel.cancel()
    print('Requeued %i messages' % requeued_messages)