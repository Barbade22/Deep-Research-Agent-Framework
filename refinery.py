
from llm import get_model

def fetch_data(question, WebSearch):
    prompt = f"""You are a precise assistant you need to get the presize information about {question}. from the website {WebSearch} 
             \n use saperators to sapearate only <BoA> in begeining and end of exact answer this is very important the answer from the rest of the your answer
             \n give me only answer of the question
             Format:
                <BoA>
                [Your answer]
                </BoA>
    (must follow the format)
    Rules:
    - You have to extract the exact answer from the website.
    - If only links are aksked give only links from webserch official pages, to help user
    - Dont mention any college name so many times
             """
    response = get_model(prompt)
    return response

def ReFT(Line: str) -> str:
    prompt = f"""Role: Professional Language Formatting Model

Task: Improve provided text and structure it in markdown format.

Input:
Text: {Line}

Output Format:
[Markdown formatted text]

Requirements:
- Clean markdown structure
- Dont mention any college name so many times
- Dont mention any college name so many times
- IF text is already well formatted in other way, modify it to markdown
- Improved language clarity
- If only links are aksked give only links from webserch official pages, to help user
- Proper punctuation and spacing
- Dont add so many fields
- You can use bullet points, numbered lists, to structure the text dont add any tables
- No explanations or additional context
- Only formatted text as output"""

    response = get_model(prompt)
    return response

def Fo(Line: str) -> str:
    prompt = f"""Role: Professional Language model for database
    you will write given text as professional language and easy to understand.
    Text: {Line} (Dont metion or explain any thing)

Rules:
- Use professional language
- Dont mention collages name so many times
- Dont mention collages name so many times
- Make the text easy to understand
- Be careful with Facts and Figures
- No need to add any additional information
- No need to explain any thing
- Write the text in a professional manner"""
    response = get_model(prompt)
    return response
# text = "AISSMS (All India Shri Shivaji Memorial Society's) College of Engineering is a private engineering college located in Pune, Maharashtra, India. The college is affiliated with the University of Pune and was founded by Chhatrapati Shri Shahu Maharaj of Kolhapur, leading to its establishment in 1992. It is situated close to the Regional Transport Office and shares its campus."
# print(Fo(text))