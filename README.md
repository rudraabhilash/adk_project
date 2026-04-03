# Python ML/AI & Web Development Workspace

This workspace is set up for machine learning, AI, and web development using Python. 

- ML/AI code: `ml_ai/main.py`
- Agent code: `ml_ai/agents/`
- Web app: `web_app/app.py`
- Requirements: `requirements.txt`

## Getting Started
1. Set up a Python virtual environment.
2. Install dependencies: `pip install -r requirements.txt`
3. Run ML/AI code: `python ml_ai/main.py`
4. Run web app: `python web_app/app.py`

#cd into ml_ai folder for sure else you will be in trouble!

#uvicorn agents.host_agent.__main__:app --port 8000 & 

#uvicorn agents.flight_agent.__main__:app --port 8001 & 

#uvicorn agents.stay_agent.__main__:app --port 8002 & 

#uvicorn agents.activities_agent.__main__:app --port 8003 & 

#streamlit run streamlit_app.py


*******************************************************************************************************************************************************************
*******************************************************************************************************************************************************************

ollama installation - 

An open-source framework designed to run large language models by Jeffrey Morgan and Michael Chiang as a part of Y Combinator's Winter 2021 batch. 
Context: The founders created Ollama to make it easier for developers to run large language models (LLMs) locally, focusing on privacy and bypassing expensive cloud APIs. 

Step 1 - Download and install binary for your OS from https://ollama.com/download

Step 2 - check version to verify - ollama --version

Step 3 - Download llama3 model. "ollama pull llama3" This downloads the model (~4–8GB depending on quantization).

Step 4 - "ollama list" to list llms.

Step 5 - "ollama run llama3" Run the model

Step 6 - Your local llm model is running! Ask questions!

Step 7 - You usually do not need to start server(http://localhost:11434) manually, but if needed: "ollama serve"

Step 8 - Officical Python client to use ollama in python code - pip install ollama

Step 9 - Sample code to run ollama via python -

{content: }

import ollama

response = ollama.chat(
    model="llama3",
    messages=[
        {"role": "user", "content": "Explain distributed locking in simple words"}
    ]
)

print(response["message"]["content"])

{content: }

Step 10 - 
*******************************************************************************************************************************************************************
*******************************************************************************************************************************************************************
