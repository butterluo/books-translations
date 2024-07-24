# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

from typing import List
import os
import json
from promptflow.core import log_metric, tool

# Define the path to the file
file_path = 'processed_results.jsonl'

@tool
def aggregate(processed_results: List[str]):
    """
    This tool aggregates the processed result of all lines and calculate the accuracy. Then log metric for the accuracy.

    :param processed_results: List of the output of line_process node.
    """
    # Check if the file exists
    if os.path.exists(file_path):
        # Delete the file
        os.remove(file_path)
        print(f"Deleted existing file: {file_path}")
    
    # Open a new .jsonl file to write
    with open('processed_results.jsonl', 'w') as file:
        # Iterate over each item in the processed_results list
        for item in processed_results:
            # Convert the item to a JSON string
            json_str = json.dumps(item)
            # Write this JSON string to the file, followed by a newline
            file.write(json_str + '\n')

    # Initialize totals
    total_elegance = 0
    total_expressiveness = 0
    total_faithfulness = 0

    # Iterate over each item in the data
    for item in processed_results:
        # Add values to totals, converting them to float
        total_elegance += float(item['elegance'])
        total_expressiveness += float(item['expressiveness'])
        total_faithfulness += float(item['faithfulness'])

    # Calculate averages
    aggregated_elegance_result = total_elegance / len(processed_results)
    aggregated_expressiveness_result = total_expressiveness / len(processed_results)
    aggregated_faithfulness_result = total_faithfulness / len(processed_results)

    # Log metric the aggregate result
    log_metric(key="elegance", value=aggregated_elegance_result)
    log_metric(key="expressiveness", value=aggregated_expressiveness_result)
    log_metric(key="faithfulness", value=aggregated_faithfulness_result)
    
    return {"elegance_aggregated_result": aggregated_elegance_result, "expressiveness_aggregated_result": aggregated_expressiveness_result,"faithfulness_aggregated_result":aggregated_faithfulness_result}
