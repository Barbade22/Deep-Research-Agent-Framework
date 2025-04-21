from worker import work
from searchengine import search_engine
from llm import get_model

# question = "Can you explain the admission process at SRM Institute of Science and Technology - College of Medicine and Health Sciences with details."
# websearch = search_engine(question)

def supervisor(question,websearch):
    worker1,worker2, worker3 = workerstack(question,websearch)
    promt = f"""Role: You are the best supervisor. You have to look at the workers output and come up with best and final answer. to the question
    Dont mention workers outputs. Just give the final answer. dont try to explin it just give the final answer. which will be final and best answer.
    Question: {question}
    Workers:
    1. Worker1 : {worker1}
    2. Worker2 : {worker2}
    3. Worker3 : {worker3}

    Requirements:
    1. You have to check the responses from the workers. 
    2. You have to get the complite answer from workes for given question.
    3. You have to give the final response. Which should be bigger.
    4. Dont explain the answer. Just give the bigger final response.
    5. if some fields are missing in the answer then dont mention those fields. answer without them.
    Only Final answer dont explain the answer. give detailed and complete answer. look for all aspects of the answer.
    """
    response = get_model(promt)
    # print("==================Worker 1================", worker1)
    # print("==================Worker 2================", worker2)
    # print("==================Worker 3================", worker3)
    return response
    

def workerstack(question,websearch):
    worker1 = work(question,websearch)

    worker2 = work(question,websearch)

    worker3 = work(question,websearch)
    return worker1,worker2,worker3

# print(workerstack(question,websearch))
# print(supervisor(question,websearch))