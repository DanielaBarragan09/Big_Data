from kafka import KafkaConsumer
import json

# Configurar el consumidor Kafka
consumer = KafkaConsumer(
    'resultados_gt2j',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda v: json.loads(v.decode('utf-8')),
    group_id='grupo_consumidor_gt2j',
    auto_offset_reset='earliest'
)

print("Esperando mensajes del tópico 'resultados_gt2j'...\n")

# Recibir mensajes
for message in consumer:
    print("Mensaje recibido:")
    print(json.dumps(message.value, indent=4, ensure_ascii=False))
