import findspark

# Locate spark testing
findspark.init()
findspark.find()

from src.insight_pipeline_package.transform import process_data
from src.insight_pipeline_package.utils import stop_active_spark_session
from create_test_session import get_test_data

def test_process_data_removes_duplicates():
    # Arrange
    data = get_test_data()

    # Act
    processed_df = process_data(data)

    # Assert
    assert processed_df.count() == data.dropDuplicates().count()
    
    stop_active_spark_session()

