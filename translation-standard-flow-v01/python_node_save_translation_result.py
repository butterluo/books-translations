import os
from dotenv import load_dotenv
from promptflow.core import tool


# translated_path = '/Users/huqianghui/Downloads/books-translations/translated-book-chunks'
translated_path = os.path.normpath(os.path.join(os.path.abspath(__file__),"..","..","translated-book-chunks"))

# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need

@tool
def my_python_tool(file_name:str,
                   first_translated_text: str=None,
                   second_translated_text: str=None,
                   final_translated_text: str=None) -> None:
    if(final_translated_text is not None):
        with open(os.path.join(translated_path, 'final-publishing-version-book-chunks', file_name), 'w',encoding='utf-8') as f:
            f.write(second_translated_text)
    
    if(second_translated_text is not None):
        with open(os.path.join(translated_path, 'second-Proofreading-version-book-churnks', file_name), 'w',encoding='utf-8') as f:
            f.write(second_translated_text)
    
    if(first_translated_text is not None):
        with open(os.path.join(translated_path, 'first-version-translated-book-chunks', file_name), 'w',encoding='utf-8') as f:
            f.write(first_translated_text)

    return None

# print(os.path.normpath(os.path.join(os.path.abspath(__file__),"..","..","translated-book-chunks")))