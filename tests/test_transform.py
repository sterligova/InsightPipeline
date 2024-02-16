from create_test_session import get_test_data
from src.insight_pipeline_package.transform import process_raw_data
from src.insight_pipeline_package.utils import stop_active_spark_session

def test_process_data_removes_duplicates():
    # Arrange
    data = get_test_data('data/raw/2024-02-13/Book1.csv')
    filtered_columns_count=13

    # Act
    processed_df = process_raw_data(data)

    # Assert
    assert processed_df.count() == filtered_columns_count
    
    stop_active_spark_session()

