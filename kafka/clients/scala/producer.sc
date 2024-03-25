import $ivy.`org.apache.kafka:kafka-clients:3.7.0`, org.apache.kafka.clients.producer._
import java.util.Properties

val props = new Properties();   
props.put("bootstrap.servers", "192.168.3.182:9092") // DEPLOY_ENV
props.put("linger.ms", 1)
props.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer")
props.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer")  

val producer = new KafkaProducer[String,String](props);
val record = new ProducerRecord[String, String]("quickstart-events-scala", "hello, i am producer from Ammonite")
producer.send(record).get
producer.flush

producer.close