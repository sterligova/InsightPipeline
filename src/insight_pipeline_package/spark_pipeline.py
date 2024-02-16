from src.insight_pipeline_package.ingest import read_data
from src.insight_pipeline_package.load import write_data
from src.insight_pipeline_package.transform import process_data
from src.insight_pipeline_package.utils import get_spark_session

def run_pipeline(input_data_file, output_path):
       spark = get_spark_session()

       print(f'Start reading data from: {input_data_file} ...')
       raw_data = read_data(input_data_file, spark)
       print('Data loaded')

       print('Start processing data...')
       processed_data = process_data(raw_data)
       print('Data processed')
       
       print('Start uploading data...')
       write_data(processed_data, output_path)
       print('Data uploaded')

