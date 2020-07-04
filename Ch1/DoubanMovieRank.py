import requests
import json

# 豆瓣电影排行
url = 'https://movie.douban.com/j/chart/top_list'
params = {
    'type': '5',
    'interval_id': '100:90',
    'action': '',
    'start': '0',
    'limit': '20'
}
header = {
    'User-Agent': 'Chrome/83.0.4103.116'
}
response = requests.get(url=url, params=params, headers=header)
content = response.json()
content1 = json.dumps(content, ensure_ascii=False)
print(content1)
