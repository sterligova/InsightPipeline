def write_data(data, output_path):
    """
    Writing data to ods or dml layers 
    
    Args:
        data:  DataFrame
        output_path: output files location
    """
    data.write.mode("overwrite").csv(output_path)