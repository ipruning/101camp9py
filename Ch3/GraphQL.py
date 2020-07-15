import requests

url = "https://gitlab.com/api/graphql"

payload = "{\"query\":\"{\\n  project(fullPath: \\\"101camp/9py/tasks\\\") {\\n    name\\n    issues {\\n      nodes {\\n        title\\n        iid\\n      }\\n    }\\n  }\\n}\\n\",\"variables\":{}}"
headers = {
    'Authorization': 'Bearer Gh9kuLv9dc3_aYsjoT-6',
    'Content-Type': 'application/json',
    'Cookie': '__cfduid=d58ab49046f0b7970f7e868d1b123004e1594820096; experimentation_subject_id=eyJfcmFpbHMiOnsibWVzc2FnZSI6IklqbG1ORGxsTUdJNUxUVmpZVGN0TkRWa1pDMDROekpsTFRJek1qTmtaRGN3WTJKaE1DST0iLCJleHAiOm51bGwsInB1ciI6ImNvb2tpZS5leHBlcmltZW50YXRpb25fc3ViamVjdF9pZCJ9fQ%3D%3D--83fd1a9228ac64bc9d13622d76fe1602b5c18053; _gitlab_session=e6b143f4adab7f12044940f4d51ff456'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
