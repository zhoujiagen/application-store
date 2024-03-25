#-*-coding: UTF-8 -*-

from kafka import KafkaConsumer
# import json

if __name__=="__main__":
  topic_name='quickstart-events-python'
  consumer = KafkaConsumer(
    topic_name,
    bootstrap_servers='192.168.3.182:9092', # DEPLOY_ENV
    group_id='kafka-python',
    max_poll_records = 100,
    # value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest'#,'smallest'
  )
  for message in consumer:
      # print(json.loads(message.value))
    print(message)

  consumer.close()