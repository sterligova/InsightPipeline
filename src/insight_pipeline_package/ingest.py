def read_data(input_data_file, spark):
		result = spark\
		    .read\
			.csv(input_data_file, header=True, inferSchema=True)
		return result