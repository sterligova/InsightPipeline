def read_data(input_data_file, spark):
		"""
    Reading data 
    
    Args:
        input_data_file: raw data file location
    """
		result = spark\
		    .read\
			.csv(input_data_file, header=True, inferSchema=True)
		return result