import os
import findspark

# Locate spark local testing
findspark.init()
findspark.find()

from src.insight_pipeline_package.utils import stop_active_spark_session
from src.insight_pipeline_package.spark_pipeline import run_pipeline
from src.insight_pipeline_package.pipeline_config import PipelineConfig

# Setup pipeline
current_dir = os.getcwd()
config = PipelineConfig()
config.input_data_file = f'{current_dir}/data/raw/2024-02-13/Book1.csv'
config.output_ods_path = f'{current_dir}/data/ods/'
config.output_dml_path = f'{current_dir}/data/dml/2024-02-13/'
config.agg_column = 'Revenue'
config.agg_column_name = 'TotalRevenue'

run_pipeline(config)
stop_active_spark_session()
