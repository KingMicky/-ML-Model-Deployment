from kafka import KafkaProducer
import json
import time
import random


KAFKA_BROKER = "localhost:9092"
TOPIC_NAME = "ml_data"

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def generate_data():
    """Simulate real-time data generation."""
    return {
        "sensor_id": random.randint(1, 10),
        "temperature": random.uniform(20.0, 30.0),
        "humidity": random.uniform(30.0, 50.0)
    }

if __name__ == "__main__":
    try:
        print(f"Sending data to Kafka topic '{TOPIC_NAME}'...")
        while True:
            data = generate_data()
            producer.send(TOPIC_NAME, value=data)
            print(f"Produced: {data}")
            time.sleep(2)  # Simulate a 2-second delay
    except KeyboardInterrupt:
        print("Producer stopped.")
    finally:
        producer.close()
