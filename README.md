# Groq AI Assistant
This project is a Streamlit web app that utilizes Groq for building an AI-powered chat assistant. It allows users to interact with the assistant by asking questions and receiving informative responses.

## Features:
  - Secure API key management using Streamlit secrets.
  - User-friendly chat interface with message history.
  - Streamlit components for a visually appealing layout.
  - Integration with Groq's large language model for generating responses.
    
## Requirements: 
  - Python 3.x
  - Streamlit 
  - Groq 
  - python-dotenv (for local development)
    ```bash
     pip install -r requirements.txt

## Installation

1. Clone the repository:
      ```bash
     git clone https://github.com/Anmol-701/AI_Chatbot.git
     cd chatbot
2. Install the required Python libraries:
    ```bash
    pip install -r requirements.txt


## Usage:

1. Create secrets.toml:
  - Create a secrets.toml file in the project directory with your Groq API key:
  ```Bash 
    [secrets]
    GROQ_API_KEY = "your_actual_api_key" 

2. Local Development (Optional):
  - Set the GROQ_API_KEY environment variable locally (if not using .env).
  - Run the app:
  ```Bash
    streamlit run app.py


# Author:
Anmol Rana