# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

from typing import List

from promptflow.core import log_metric, tool


@tool
def aggregate(processed_results: List[str]):
    """
    This tool aggregates the processed result of all lines and calculate the accuracy. Then log metric for the accuracy.

    :param processed_results: List of the output of line_process node.
    """

    # Add your aggregation logic here
    # Aggregate the results of all lines and calculate the elegance,expressiveness,faithfulness
    aggregated_elegance_result = round((processed_results.count("elegance") / len(processed_results)), 2)
    aggregated_expressiveness_result = round((processed_results.count("expressiveness") / len(processed_results)), 2)
    aggregated_faithfulness_result = round((processed_results.count("faithfulness") / len(processed_results)), 2)
    # Log metric the aggregate result
    log_metric(key="elegance", value=aggregated_elegance_result)
    log_metric(key="expressiveness", value=aggregated_expressiveness_result)
    log_metric(key="faithfulness", value=aggregated_faithfulness_result)
    
    return {"elegance_aggregated_result": aggregated_elegance_result, "expressiveness_aggregated_result": aggregated_expressiveness_result,"faithfulness_aggregated_result":aggregated_faithfulness_result}
