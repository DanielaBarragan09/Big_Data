# Proyecto: Análisis de Datos con Apache Spark, Hadoop y Kafka

## Descripción General
Este proyecto realiza un **análisis de datos** sobre el archivo `gt2j-8ykr.csv` usando **Apache Spark** y envía los resultados a un tópico en **Apache Kafka** para su posterior consumo.

---

## Arquitectura de la Solución
+-------------------+
| Fuente CSV |
| gt2j-8ykr.csv |
+---------+---------+
|
v
+-------------------+
| Apache Spark |
| (Lectura y |
| procesamiento) |
+---------+---------+
|
v
+-------------------+
| Apache Kafka |
| (Tópico: |
| resultados_gt2j) |
+---------+---------+
|
v
+-------------------+
| Consumer Python |
| (Lectura de |
| mensajes Kafka) |
+-------------------+


---

## Requisitos

- Python 3.9+
- Apache Spark
- Hadoop (con HDFS activo)
- Apache Kafka (corriendo en localhost:9092)
- Java JDK 8 o superior

---

## Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/Tarea-33.git
   cd "Tarea 33"

   python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

pip install -r requirements.txt
