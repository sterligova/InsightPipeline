import findspark

# Locate spark testing
findspark.init()
findspark.find()

from pyspark.sql import SparkSession

def get_test_data():
    spark_session = SparkSession.builder.appName('test').getOrCreate()
    return spark_session.read.csv('data/raw/2024-02-13/Book1.csv', header=True, inferSchema=True)