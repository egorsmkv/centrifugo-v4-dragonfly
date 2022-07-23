import json
import requests
import random
import time

for _ in range(1, 100):
    command = {
        "method": "publish",
        "params": {
            "channel": "events", 
            "data": {
                "ts": str(time.time()),
                "content": f"event_{random.randint(100_000, 999_999)}"
            }
        }
    }

    api_key = "55aafd5e-2abb-4bfc-b419-9cd5148769f7"
    data = json.dumps(command)
    headers = {'Content-type': 'application/json', 'Authorization': 'apikey ' + api_key}
    resp = requests.post("http://localhost:8000/api", data=data, headers=headers)
    print(resp.json())
