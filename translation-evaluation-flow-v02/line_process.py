# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
import os
from dotenv import load_dotenv
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

    if "OPENAI_API_KEY" not in os.environ and "AZURE_OPENAI_API_KEY" not in os.environ:
        # load environment variables from .env file
        load_dotenv()

    prjroot = os.path.normpath(os.path.join(os.path.abspath(__file__),"..",".."))
    # Add your line processing logic here
    elegance_prompty = Prompty.load(source=os.path.normpath(os.path.join(os.path.abspath(__file__),"..","prompty","elegance.prompty")))
    expressiveness_prompty = Prompty.load(source=os.path.normpath(os.path.join(os.path.abspath(__file__),"..","prompty","expressiveness.prompty")))
    faithfulness_prompty = Prompty.load(source=os.path.normpath(os.path.join(os.path.abspath(__file__),"..","prompty","faithfulness.prompty")))
    
    #/Users/huqianghui/Downloads/books-translations/books/TheInnovatorsDilemmaWhenNewTechnoloClaytonMChristensen-chart1.md
    original_english_context_file_path = os.path.join(prjroot, "books",original_english_context_file_path)
    with open(original_english_context_file_path, 'r', encoding='utf-8') as original_english_context_file:
        original_english_context = original_english_context_file.read()

    #/Users/huqianghui/Downloads/books-translations/book-chunks/TheInnovatorsDilemmaWhenNewTechnoloClaytonMChristensen-chart1-00.md
    current_english_chart_file_path = os.path.join(prjroot, "book-chunks",current_english_chart_file_path)
    with open(current_english_chart_file_path, 'r', encoding='utf-8') as current_english_chart_file:
        current_english_chart = current_english_chart_file.read()

    #/Users/huqianghui/Downloads/books-translations/translated-book-chunks/final-publishing-version-book-chunks/TheInnovatorsDilemmaWhenNewTechnoloClaytonMChristensen-chart1-00.md
    translated_chinese_text_file_path = os.path.join(prjroot, "translated-book-chunks", "final-publishing-version-book-chunks", translated_chinese_text_file_path)
    with open(translated_chinese_text_file_path, 'r', encoding='utf-8') as translated_chinese_text_file:
        translated_chinese_text = translated_chinese_text_file.read()

    eleganceScore = elegance_prompty(original_english_context=original_english_context,current_english_chart=current_english_chart,translated_chinese_text=translated_chinese_text)
    expressivenessScore = expressiveness_prompty(original_english_context=original_english_context,current_english_chart=current_english_chart,translated_chinese_text=translated_chinese_text)
    faithfulnessScore = faithfulness_prompty(original_english_context=original_english_context,current_english_chart=current_english_chart,translated_chinese_text=translated_chinese_text)

    return {"elegance": eleganceScore, "expressiveness": expressivenessScore,"faithfulness":faithfulnessScore}