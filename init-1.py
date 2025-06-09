import requests
import json

url = "http://localhost:11434/api/generate"
data = {
    "model": "gemma3:4b",
    "prompt": "Give me a joke about AI. in less than 20 words.",
}

response = requests.post(url, json=data, stream=True)

if response.status_code == 200:
    for line in response.iter_lines():
        if line:
            decoded_line = line.decode('utf-8')
            try:
                json_line = json.loads(decoded_line)
                print(json_line)
            except json.JSONDecodeError:
                print(f"Error decoding JSON: {decoded_line}")   
else:
    print(f"Error: Received status code {response.status_code} from the server.")
    print("Response content:", response.text)
                