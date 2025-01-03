from kafka import KafkaConsumer
import requests
import json


KAFKA_BROKER = "localhost:9092"
TOPIC_NAME = "ml_data"
API_URL = "http://localhost:8000/predict"


consumer = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers=KAFKA_BROKER,
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

def send_to_model(data):
    """Send data to the ML API for prediction."""
    try:
        response = requests.post(API_URL, json=data)
        print(f"Prediction: {response.json()}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending data to API: {e}")


if __name__ == "__main__":
    print(f"Listening for messages on topic '{TOPIC_NAME}'...")
    for message in consumer:
        print(f"Consumed: {message.value}")
        send_to_model(message.value)
