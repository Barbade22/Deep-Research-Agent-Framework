from worker import work
from searchengine import search_engine
from llm import get_model
from supervoiser import supervisor
# question = "Can you explain the admission process at SRM Institute of Science and Technology - College of Medicine and Health Sciences with details."
# websearch = search_engine(question)

def validate(question,websearch):
    # worker1,worker2, worker3 = workerstack(question,websearch)
    respons = supervisor(question,websearch)
    promt = f"""Role: You are the validator you have to look at the Reaponse and correct it based on websearch results and give the final answer.
    Question: 
    {question}
    Websearch: 
    {websearch}
    Response:
    {respons}
    Resquirements:
    -Your final response should be well explined and only look for minor corrections.
    -Dont metion any college name so many times.
    -Give Refrences links in final answer for every.
    -Use professional language.
    -Be careful with Facts and Figures.
    -No need for irrelevant information.
    -Look for the facts from websearch and correct the response inaccuracies.
    -You have to correct the response based on websearch results.
    -You have to give the big final response.
    -Dont explain the answer. Just give the big final response.
    -If some fields are missing in the answer then dont mention those fields. answer without them.
    -Keep refrerence links.

    Answer Formatt:
    [Your final response]
    Ref: 
    [All information sources,Reference links]
    """
    # print("=================Suprevisor=================",respons)
    response = get_model(promt)
    return response
    

# print(workerstack(question,websearch))
# print(supervisor(question,websearch))