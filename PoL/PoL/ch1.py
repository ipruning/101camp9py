import argparse
import requests
import json


from . import api

get_path()
config_name = "Alex.json"
config_path = package_path + "/configs/" + config_name

with open(config_path, "r") as load_config:
    config = json.load(load_config)
    print(config)
    print(config["gitlab_tokens"])


def get_branch():
    url = (
        "https://gitlab.com/api/v4/projects/18907382/repository/branches?private_token="
        "Gh9kuLv9dc3_aYsjoT-6&page=1&per_page=50"
    )
    result = requests.get(url)
    get_branch_data = result.json()
    get_branch_list = []
    for branch in get_branch_data:
        name = branch["name"]
        if name != "master":
            get_branch_list.append(name)
    return get_branch_list


# cli = input()
# while cli != 'pol -exit':
#     if cli == 'pol -branch':
#         branch_data = get_branch()
#         for branch_name in branch_data:
#             print(branch_name)
#         print('\nThe number of branches is {}.'.format(len(branch_data)))
#         cli = input()
# input('logout')
# exit()

parser = argparse.ArgumentParser(description="Proof of Learning")
parser.add_argument("API", metavar="N", type=int, help="API Key")

args = parser.parse_args()
print(args.API)

branch_data = get_branch()
for branch_name in branch_data:
    print(branch_name)
print("\nThe number of branches is {}.".format(len(branch_data)))
