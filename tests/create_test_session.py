from pyspark.sql import SparkSession

spark_session = SparkSession.builder.appName('test').getOrCreate()
raw_data = spark_session.read.csv('data/raw/2024-02-13/Book1.csv', header=True, inferSchema=True)