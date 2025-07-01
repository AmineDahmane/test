import requests
import json

response = requests.post("http://localhost:11434/api/generate", json={
    "model": "llama2",
    "prompt": "Explain how recursion works in programming"
})

# Print the raw text to inspect
print(response.text)

# Split the response into separate JSON objects
json_objects = response.text.strip().split('\n')

for obj in json_objects:
    if obj:
        data = json.loads(obj)
        print(data.get("response", "No 'response' key found"))
