#-*-coding: UTF-8 -*-

from testcontainers.kafka import KafkaContainer
from kafka import KafkaProducer
from kafka import KafkaConsumer
from kafka.errors import KafkaError

if __name__=="__main__":
  with KafkaContainer(image="confluentinc/cp-kafka:5.4.3") as kafka:
    bootstrap_servers = kafka.get_bootstrap_server()
    print(bootstrap_servers)

    # producer: kafka\clients\python\producer.py
    topic_name='quickstart-events-python'
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
    f = producer.send(topic_name, b'hello, i am producer from kafka-python')
    try:
      record_metadata = f.get(timeout=3)
      print(record_metadata)
    except KafkaError as e:
      print(e)
    producer.flush()
    producer.close()

    # consumer: kafka\clients\python\consumer.py
    topic_name='quickstart-events-python'
    consumer = KafkaConsumer(
      topic_name,
      bootstrap_servers=bootstrap_servers,
      group_id='kafka-python',
      max_poll_records = 100,
      # value_deserializer=lambda m: json.loads(m.decode('utf-8')),
      auto_offset_reset='earliest'#,'smallest'
    )
    for message in consumer:
        # print(json.loads(message.value))
      print(message)
      break

    consumer.close()