import os
import findspark

# Locate spark local testing
findspark.init()
findspark.find()

from src.insight_pipeline_package.utils import stop_active_spark_session
from src.insight_pipeline_package.spark_pipeline import run_pipeline


current_dir = os.getcwd()

input_data_path =  f'{current_dir}/data/raw/2024-02-13/Book1.csv'
output_path = f'{current_dir}/data/ods/2024-02-13/'

run_pipeline(input_data_path, output_path)

stop_active_spark_session()