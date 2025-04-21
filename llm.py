import requests
import json

def get_model(prompt):
    # Define the URL and model name
    url = "http://localhost:11434/api/generate"
    model = "llama3.2:3b"
    # model = "llama3.2:latest"
    # model = "llama3.2:3b-instruct-q8_0"
    # model = "phi4:latest"
    # model = "qwen2.5-coder:32b-instruct-q4_0"
    
    # Define headers and prepare the payload
    headers = {"Content-Type": "application/json"}
    payload = {
        "model": model,  # Model name
        "prompt": prompt  # User's input prompt
    }

    try:
        # Send the POST request to the Ollama API
        response = requests.post(url, headers=headers, data=json.dumps(payload))

        # Check if the request was successful
        if response.status_code == 200:
            # Print raw content to check the response format
            raw_response = response.content.decode('utf-8')

            # Split the raw response by newlines to process each JSON object
            json_objects = raw_response.split("\n")

            # Variable to accumulate the response
            full_response = []

            # Iterate over each chunk and try to parse it as JSON
            for json_chunk in json_objects:
                if json_chunk.strip():  # Skip empty chunks
                    try:
                        parsed_response = json.loads(json_chunk)
                        # Extract the response text and append to the full response
                        model_response = parsed_response.get('response', '')
                        if model_response:
                            full_response.append(model_response)
                    except json.JSONDecodeError:
                        print(f"Failed to decode JSON chunk: {json_chunk}")

            # Join all parts to form the full response
            return "".join(full_response)
        else:
            return f"Request failed with status code {response.status_code}. Response: {response.text}"
    except Exception as e:
        return f"An error occurred: {e}"
