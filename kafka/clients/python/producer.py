#-*-coding: UTF-8 -*-

from kafka import KafkaProducer
from kafka.errors import KafkaError
import logging

if __name__=="__main__":
  topic_name='quickstart-events-python'
  producer = KafkaProducer(bootstrap_servers='192.168.3.182:9092') # DEPLOY_ENV
  f = producer.send(topic_name, b'hello, i am producer from kafka-python')
  try:
    record_metadata = f.get(timeout=3)
  except KafkaError as e:
    logging.error("timeout", exc_info=e)
  producer.flush()
  producer.close()