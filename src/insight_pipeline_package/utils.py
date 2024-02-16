from pyspark.sql import SparkSession


def get_spark_session(name: str) -> SparkSession:
    """
    Create spark session 
    
    Args:
        name: SparkSession name
    """
    session = SparkSession.builder \
                    .appName(name) \
                    .getOrCreate()
    return session

def stop_active_spark_session():
    """
    Stop active spark session 
    """
    spark: SparkSession = SparkSession.getActiveSession()
    if spark:
       print('Closing spark session...')
       spark.stop()
       print('Spark session closed')
    else:
        print('No active session found !!!')

