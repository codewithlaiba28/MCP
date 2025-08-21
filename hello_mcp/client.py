import requests

url = "http://localhost:8000/mcp/"

headers = {
    "Accept": "application/json,text/event-stream" ,
}

body = {
    "jsonrpc": "2.0",
    "method": "tools/call",
    "params": {
        "name": "search_online",
        "arguments":{
            "query" :"What is the weather like today?"
        }
        
     },
     "id" : 1
}
response = requests.post(url, headers=headers , json=body)
print(response.text)
print("-"* 100)

# for line in response.iter_lines():
#     if line:
#         print(line)