import os
import requests
import json
from dotenv import load_dotenv

def country_specific_recommendations(country, improvement_areas):
    
    # Get the absolute path of the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Specify the relative path to your .env file
    dotenv_path = os.path.join(current_dir, "..", ".env")

    # Load environment variables from the .env file
    load_dotenv(dotenv_path)

    # Define the API endpoint
    api_url = "https://api.openai.com/v1/chat/completions"

    # Set your OpenAI API key
    api_key = os.getenv("OPEN_AI_API_KEY")

    # Define the message input with the article summary
    prompt = f"""
    You are an expert in developing digital channels and helplines through which children can be safe with specific domain knowledge for {country}. Provide the most important recommendation in specific to this country's context to improve in each of these areas (1 detailed and country-specific recommendation per area): {improvement_areas}. Please return your recommendations as code  with the streamlit formatting below:
    with st.expander("1. Recommendation 1 Title - Improvement Area Name"):
        st.write("Recommendation 1 text")
    """

    # Define the API call payload
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 400,
        "temperature": 0.5,
        # "stop": "###",
        "n": 1,
        # "presence_penalty": 0.6,
        # "frequency_penalty": 0.2
    }

    # Make the API call
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }

    response = requests.post(api_url, headers=headers, json=payload)

    # Parse and print the generated message
    data = response.json()
    message = data["choices"][0]["message"]["content"]
    
    return message