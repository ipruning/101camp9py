import requests
import json


class QueryGraphQL(object):
    def __init__(self, name, query, variables):
        super(QueryGraphQL, self).__init__()
        self.name = name
        self.query = query
        self.variables = variables
        with open("./configs/default.json", 'r') as load_config:
            config = json.load(load_config)
        self.headers = {"Authorization": config['gitlab_tokens']}

    def run_query(self):  # 查询
        response = requests.post('https://gitlab.com/api/graphql',
                                 json={
                                     'query': self.query,
                                     'variables': self.variables
                                 },
                                 headers=self.headers)
        if response.status_code == 200:
            return response.json()  # 返回查询结果
        else:
            raise Exception(
                "Query failed to run by returning code of {}. {}".format(
                    response.status_code, self.query))

    def print_query(self):  # 打印查询结果
        print(self.run_query())

    def save_query(self):  # 保存查询结果
        with open('./docs/' + self.name + '.json', 'w') as json_file:
            # json.dump(result, json_result)
            json.dump(self.run_query(), json_file, ensure_ascii=False)


class QueryREST(object):
    def __init__(self, name, url):
        super(QueryREST, self).__init__()
        self.name = name
        self.url = url
        with open("./configs/default.json", 'r') as load_config:
            config = json.load(load_config)
            self.headers = {"Authorization": config['gitlab_tokens']}
        self.payload = {}

    def run_query(self):
        response = requests.request("GET",
                                    self.url,
                                    headers=self.headers,
                                    data=self.payload)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(
                "Query failed to run by returning code of {}. {}".format(
                    response.status_code, self.url))

    def save_query(self):
        with open('./docs/' + self.name + '.json', 'w') as json_file:
            # json.dump(result, json_result)
            json.dump(self.run_query(), json_file, ensure_ascii=False)
