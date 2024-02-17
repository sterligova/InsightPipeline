import os
import findspark
import sys

# Locate spark local testing
findspark.init()
findspark.find()

# add src to import scripts
sys.path.insert(1, './src/')

from insight_pipeline.utils import stop_active_spark_session
from insight_pipeline.spark_pipeline import run_pipeline
from insight_pipeline.pipeline_config import PipelineConfig

# Setup pipeline
current_dir = os.getcwd()
config = PipelineConfig()
config.session_name = 'RunApp'
config.input_data_file = f'{current_dir}/data/raw/2024-02-13/Book1.csv'
config.output_ods_path = f'{current_dir}/data/ods/'
config.output_dml_path = f'{current_dir}/data/dml/2024-02-13/'
config.agg_column = 'Revenue'
config.grb_column = 'Product'

run_pipeline(config)
stop_active_spark_session()
