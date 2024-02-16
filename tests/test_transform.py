import findspark

# Locate spark testing
findspark.init()
findspark.find()

from src.insight_pipeline_package.transform import process_data
from src.insight_pipeline_package.utils import stop_active_spark_session
from create_test_session import raw_data


def test_process_data_removes_duplicates():
    # Apply the process_data function
    processed_df = process_data(raw_data)

    # Check if duplicates are removed
    assert processed_df.count() == raw_data.dropDuplicates().count()

stop_active_spark_session()