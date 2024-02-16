def write_data(processed_data, output_path):
    processed_data.write.mode("overwrite").csv(output_path)