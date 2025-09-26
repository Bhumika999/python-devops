from flask import Flask
import os
import requests
from requests.auth import HTTPBasicAuth
import json

app = Flask(__name__)

@app.route('/createJIRA' , methods=['POST'])
def createJIRA():
    url = "https://bhumikagupta999.atlassian.net/rest/api/3/issue"

    API_TOKEN = os.getenv("api_token_github")

    auth = HTTPBasicAuth("bhumikagupta999@gmail.com", API_TOKEN)

    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
    }

    payload = json.dumps( {
        "fields": {
            "description": {
            "content": [
                {
                "content": [
                    {
                    "text": "My first jira ticket",
                    "type": "text"
                    }
                ],
                "type": "paragraph"
                }
            ],
            "type": "doc",
            "version": 1
            },
            "project": {
            "key": "SCRUM"
            },
            "issuetype": {
            "id": "10005"
            },
            "summary": "First JIRA Ticket",
        },
        "update": {}
    } )
    
    #  webhook = request.json
    #  response = None
    # if webhook['comment'].get('body') == "/jira":
    response = requests.request(
    "POST",
    url,
    data=payload,
    headers=headers,
    auth=auth
    )
    return(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
    
    # else:
    #     print('Jira issue will be created if comment include /jira')

if __name__ == '__main__':
    app.run("0.0.0.0")