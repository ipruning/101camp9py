import requests
import json

url = 'https://fanyi.baidu.com/sug'
kw = input('Translate: ')
kw = {'kw': kw}
header = {'User-Agent': 'Chrome/83.0.4103.116'}
response = requests.post(url=url, data=kw, headers=header)
response.raise_for_status()
response.encoding = response.apparent_encoding
content_json = response.json()
content = json.dumps(content_json, ensure_ascii=False)
result = json.loads(content)
print(result["data"])
