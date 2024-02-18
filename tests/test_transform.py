from tests.create_test_session import get_test_data
from src.insight_pipeline.transform import process_raw_data, process_odl_data
from src.insight_pipeline.utils import stop_active_spark_session

def test_process_data_removes_duplicates():
    # Arrange
    data = get_test_data('data/raw/2024-02-13/Book1.csv')
    expected_rows_count = 13

    # Act
    processed_df = process_raw_data(data)

    # Assert
    assert processed_df.count() == expected_rows_count
    
    stop_active_spark_session()


def test_process_data_aggregate():
    # Arrange
    data = get_test_data('data/raw/2024-02-14/Book2.csv')
    expected_rows_count = 5
    agg_column = 'Revenue'
    grb_column = 'Product'

    # Act
    processed_df = process_odl_data(data, grb_column, agg_column)

    # Assert
    assert processed_df.count() == expected_rows_count
    
    stop_active_spark_session()

