import findspark

# Locate spark testing
findspark.init()
findspark.find()

from pyspark.sql import SparkSession
def get_test_data(file):
    spark_session = SparkSession.builder.appName('test').getOrCreate()
    return spark_session.read.csv(file, header=True, inferSchema=True)