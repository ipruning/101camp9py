import requests

def get_branch():
    url = 'https://gitlab.com/api/v4/projects/18907382/repository/branches?private_token=' \
          'Gh9kuLv9dc3_aYsjoT-6&page=1&per_page=50'
    result = requests.get(url)
    get_branch_data = result.json()
    get_branch_list = []
    for branch in get_branch_data:
        name = branch['name']
        if name != 'master':
            get_branch_list.append(name)
    return get_branch_list

cli = input()
while cli != 'pol -exit':
    if cli == 'pol -branch':
        branch_data = get_branch()
        for branch_name in branch_data:
            print(branch_name)
        print('\nThe number of branches is {}.'.format(len(branch_data)))
        cli = input()
input('logout')
exit()
