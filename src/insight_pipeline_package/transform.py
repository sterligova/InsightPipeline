from src.insight_pipeline_package.pipeline_config import PipelineConfig
from pyspark.sql.functions import col, when, sum

def filter_dublicates_na(data):
    # Remove duplicates
    filtered_data = data.dropDuplicates()

    # Replace empty values with Null
    for column in filtered_data.columns:
        filtered_data = filtered_data.withColumn(column, \
            when(col(column) == "", None).otherwise(col(column)))

    # Drop rows with mostly Null values
    filtered_data = filtered_data.na.drop()
    return filtered_data

def aggregate_data(data, agg_column:str, agg_column_name:str):
    data = data.withColumn(agg_column , data[agg_column].cast('int'))
    
    # Aggregation
    agg_data = data.groupBy("Product").agg(sum(agg_column).alias(agg_column_name))

    return agg_data

def process_raw_data(raw_data):
    filtered_data = filter_dublicates_na(raw_data)

    return filtered_data


def process_odl_data(odl_data, config: PipelineConfig):
    aggregated_data = aggregate_data(odl_data, config.agg_column, config.agg_column_name)

    return aggregated_data