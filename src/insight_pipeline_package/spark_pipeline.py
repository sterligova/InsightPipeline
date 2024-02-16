from pyspark.sql import SparkSession


def get_spark_session() -> SparkSession:
    session = SparkSession.builder \
                    .appName("AppName") \
                    .getOrCreate()
    return session


def read_data(input_data_file, spark):
		result = spark\
		    .read\
			.csv(input_data_file, header=True, inferSchema=True)
		return result


def process_data(raw_data):
    # process data here
    return raw_data


def write_data(processed_data, output_path):
    processed_data.write.csv(output_path)


def run_pipeline(input_data_file, output_path):
       spark = get_spark_session()
       
       raw_data = read_data(input_data_file, spark)
      
       processed_data = process_data(raw_data)
       
       write_data(processed_data, output_path)

