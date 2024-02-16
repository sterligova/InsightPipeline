from pyspark.sql import SparkSession


def get_spark_session() -> SparkSession:
    session = SparkSession.builder \
                    .appName("AppName") \
                    .getOrCreate()
    return session
