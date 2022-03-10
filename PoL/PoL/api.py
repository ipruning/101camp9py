import requests
import json
import os
from pathlib import Path

print("Running" if __name__ == "__main__" else "Importing", Path(__file__).resolve())


def get_path():
    global package_path  # https://www.w3schools.com/python/python_variables_global.asp
    package_path = os.path.realpath(__file__)[:-11]
    # print("package_path: ", package_path)


get_path()
config_name = "Alex.json"
config_path = f'{package_path}/configs/{config_name}'


class QueryGraphQL(object):
    def __init__(self, name, query, variables):
        super(QueryGraphQL, self).__init__()
        self.name = name
        self.query = query
        self.variables = variables
        with open(config_path, "r") as load_config:
            config = json.load(load_config)
        self.headers = {"Authorization": config["gitlab_tokens"]}

    def run_query(self):  # 查询
        response = requests.post(
            "https://gitlab.com/api/graphql",
            json={"query": self.query, "variables": self.variables},
            headers=self.headers,
        )
        if response.status_code == 200:
            return response.json()  # 返回查询结果
        else:
            raise Exception(
                "Query failed to run by returning code of {}. {}".format(
                    response.status_code, self.query
                )
            )

    def print_query(self):  # 打印查询结果
        print(self.run_query())

    def save_query(self):  # 保存查询结果
        with open(f'{package_path}/docs/{self.name}.json', "w") as json_file:
            # json.dump(result, json_result)
            json.dump(self.run_query(), json_file, ensure_ascii=False)


class QueryREST(object):
    def __init__(self, name, url):
        super(QueryREST, self).__init__()
        self.name = name
        self.url = url
        with open(config_path, "r") as load_config:
            config = json.load(load_config)
            self.headers = {"Authorization": config["gitlab_tokens"]}
        self.payload = {}

    def run_query(self):
        response = requests.request(
            "GET", self.url, headers=self.headers, data=self.payload
        )
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(
                "Query failed to run by returning code of {}. {}".format(
                    response.status_code, self.url
                )
            )

    def save_query(self):
        with open(f'{package_path}/docs/{self.name}.json', "w") as json_file:
            # json.dump(result, json_result)
            json.dump(self.run_query(), json_file, ensure_ascii=False)
