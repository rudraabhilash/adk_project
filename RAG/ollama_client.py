
import ollama

response = ollama.chat(
    model="llama3",
    messages=[
        {"role": "user", "content": "Let's see full documentation for Ollama Python client. Kya kehna hai aapka?"},
    ]
)

print(response["message"]["content"])



# Alternate use via REST API
import requests

url = "http://localhost:11434/api/generate"

data = {
    "model": "llama3",
    "prompt": "Explain caching strategies",
    "stream": False
}

response = requests.post(url, json=data)
print(response.json()["response"])