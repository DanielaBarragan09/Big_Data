from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, count
from kafka import KafkaProducer
import json

# Crear la sesión de Spark
spark = SparkSession.builder \
    .appName("AnalisisGT2J") \
    .config("spark.hadoop.fs.defaultFS", "hdfs://localhost:9000") \
    .config("spark.sql.shuffle.partitions", "4") \
    .getOrCreate()

# Cargar el CSV desde HDFS o local
data_path = "data/gt2j-8ykr.csv"
df = spark.read.csv(data_path, header=True, inferSchema=True)

# Mostrar esquema
print("Esquema de datos:")
df.printSchema()

# Procesamiento simple (ejemplo: promedio de edad por sexo)
resultado = df.groupBy("sexo").agg(
    avg(col("edad")).alias("edad_promedio"),
    count(col("edad")).alias("total_registros")
)

print("Resultado del análisis:")
resultado.show()

# Convertir resultado a JSON
result_json = [row.asDict() for row in resultado.collect()]

# Enviar resultado a Kafka
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

producer.send('resultados_gt2j', result_json)
producer.flush()
producer.close()

print("Datos enviados al tópico 'resultados_gt2j' en Kafka.")

spark.stop()
