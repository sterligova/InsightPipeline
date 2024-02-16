class PipelineConfig:
    # spark session name
    session_name: str

    # raw data file location
    input_data_file: str

    # path to operational data store (ods) layer
    output_ods_path: str

    # path to data mart layer
    output_dml_path: str

    # column name for data aggregation sum
    agg_column: str

    # column name for data group by
    grb_column: str
