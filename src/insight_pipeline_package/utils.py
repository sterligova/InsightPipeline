from pyspark.sql import SparkSession


def get_spark_session() -> SparkSession:
    session = SparkSession.builder \
                    .appName("AppName") \
                    .getOrCreate()
    return session

def stop_active_spark_session():
    spark: SparkSession = SparkSession.getActiveSession()
    if spark:
       print('Closing spark session...')
       spark.stop()
       print('Spark session closed')
    else:
        print('No active session found !!!')

