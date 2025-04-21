from refinery import fetch_data
from searchengine import search_engine
# from refinery import extract_answer

def work(question,websearch):
    # websearch = search_engine(question)
    response = fetch_data(question, websearch)
    return response

