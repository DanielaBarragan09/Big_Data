# Proyecto: Análisis de Datos con Apache Spark, Hadoop y Kafka

## Descripción
Este proyecto realiza un análisis sobre el archivo **gt2j-8ykr.csv** utilizando **Apache Spark**, con almacenamiento en **HDFS (Hadoop)** y comunicación de resultados a **Kafka**.

## Arquitectura de la Solución

**1. Fuente de Datos:**  
Archivo `gt2j-8ykr.csv` almacenado en HDFS o en la carpeta local `/data`.

**2. Procesamiento:**  
Ejecutado con **Apache Spark**:
- Lectura del CSV.
- Cálculo de métricas (por ejemplo, promedio de edad por sexo).
- Serialización de resultados en JSON.

**3. Comunicación:**  
Resultados enviados a un tópico Kafka (`resultados_gt2j`).

**4. Visualización:**  
- Monitor en `http://localhost:4040` (Spark UI).
- Kafka Consumer opcional para recibir resultados.

## Ejecución

```bash
# Crear entorno virtual (opcional)
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar script
spark-submit src/main.py
