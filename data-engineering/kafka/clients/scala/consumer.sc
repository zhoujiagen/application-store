import $ivy.`org.apache.kafka:kafka-clients:3.7.0`, org.apache.kafka.clients.consumer._
import java.util.Properties
import java.util.Arrays
import java.time.Duration

val props = new Properties();
props.setProperty("bootstrap.servers", "192.168.3.182:9092");
props.setProperty("group.id", "Ammonite");
props.setProperty("enable.auto.commit", "true");
props.setProperty("auto.commit.interval.ms", "1000");
props.setProperty("key.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
props.setProperty("value.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");

val consumer = new KafkaConsumer[String,String](props);
consumer.subscribe(Arrays.asList("quickstart-events-scala"));

while (true) {
    val records = consumer.poll(Duration.ofMillis(100));
    records.forEach(record => System.out.printf("offset = %d, key = %s, value = %s%n", record.offset(), record.key(), record.value()))
}