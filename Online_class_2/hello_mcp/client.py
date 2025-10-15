import requests

url = "http://localhost:8000/mcp/"

headers = {
    "Accept": "application/json,text/event-stream",
}

body = {
    "jsonrpc": "2.0",
    "method" : "tools/call",
    "id" : 1,
    "params" : {
        "name": "search_online",
        "arguments":{
            "query": "What is the capital of France?"
        }
    }
}

response = requests.post(url, json=body, headers=headers, stream=True)

print("_"*100)
print(f"Reponse: {response.text}" )

for line in response.iter_lines():
    if line:
        print(line)
