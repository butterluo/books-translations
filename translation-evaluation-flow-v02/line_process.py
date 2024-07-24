# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

from promptflow.core import tool
from promptflow.core import Prompty


@tool
def line_process(original_english_context_file_path: str, current_english_chart_file_path: str,translated_chinese_text_file_path: str) -> dict[str:float]:
    """
    This tool processes the prediction of a single line and returns the processed result.

    :param original_english_context: the entrire chart context file path.
    :param current_english_chart_file_path: the current chart english context file path.
    :param translated_chinese_text: the translated chinese text of the current context file path.
    """

    # Add your line processing logic here
    elegance_prompty = Prompty.load(source="/Users/huqianghui/Downloads/books-translations/translation-evaluation-flow-v01/prompty/elegance.prompty")
    expressiveness_prompty = Prompty.load(source="/Users/huqianghui/Downloads/books-translations/translation-evaluation-flow-v01/prompty/expressiveness.prompty")
    faithfulness_prompty = Prompty.load(source="/Users/huqianghui/Downloads/books-translations/translation-evaluation-flow-v01/prompty/faithfulness.prompty")

    with open(original_english_context_file_path, 'r', encoding='utf-8') as original_english_context_file:
        original_english_context = original_english_context_file.read()

    with open(current_english_chart_file_path, 'r', encoding='utf-8') as current_english_chart_file:
        current_english_chart = current_english_chart_file.read()

    with open(translated_chinese_text_file_path, 'r', encoding='utf-8') as translated_chinese_text_file:
        translated_chinese_text = translated_chinese_text_file.read()

    eleganceScore = elegance_prompty(original_english_context=original_english_context,current_english_chart=current_english_chart,translated_chinese_text=translated_chinese_text)
    expressivenessScore = expressiveness_prompty(original_english_context=original_english_context,current_english_chart=current_english_chart,translated_chinese_text=translated_chinese_text)
    faithfulnessScore = faithfulness_prompty(original_english_context=original_english_context,current_english_chart=current_english_chart,translated_chinese_text=translated_chinese_text)

    return {"elegance": eleganceScore, "expressiveness": expressivenessScore,"faithfulness":faithfulnessScore}