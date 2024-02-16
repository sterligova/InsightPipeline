from pyspark.sql.functions import col, when


def process_data(raw_data):
    # Remove duplicates
    processed_data = raw_data.dropDuplicates()

    # Replace empty values with Null
    for column in processed_data.columns:
        processed_data = processed_data.withColumn(column, \
            when(col(column) == "", None).otherwise(col(column)))

    # Drop rows with mostly Null values
    # processed_data = processed_data.na.drop(how='any')
        
    # Drop rows with more than 50% null values
    #processed_data = processed_data.na.drop(thresh=len(processed_data.columns) / 2)

    return processed_data


