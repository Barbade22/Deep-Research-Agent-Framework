from tavily import TavilyClient
# from refinery import fetch_data, extract_answer

def search_engine(query):
    # Initialize the Tavily client with your API key
    tavily_client = TavilyClient(api_key="Your_API_Key_Here")  # Replace with your actual API key

    # Execute a search query
    response = tavily_client.search(query,search_depth="advanced",max_results=10)
    # response = tavily_client.search(query)
    return response

## USing DUCKDUCKGO API (Free)
# from duckduckgo_search import DDGS  # Import the correct DuckDuckGo search class
# def search_engine(query):
#     # search_Q = "Admission process of SRM Institute of Science and Technology - College of Medicine and Health Sciences?"
#     search_Q = query
#     with DDGS() as ddgs:
#         results = ddgs.text(
#             search_Q,
#             max_results=5,
#             region="in"  # Use lowercase "in" for India
#         )
#     return results
    # print(results)