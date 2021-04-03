from nose.tools import *
from pol import api


def test_QueryGraphQL():
    query = """
    {
    project(fullPath: "101camp/2py/tasks") {
        id
    }
    }
    """
    issue = api.QueryGraphQL("101camp9py-id", query, {})
    assert_equal(issue.run_query()['data']['project']['id'],
                 "gid://gitlab/Project/13020942")


def test_QueryREST():
    branch = api.QueryREST(
        "101camp9py-branch",
        "https://gitlab.com/api/v4/projects/18907382/repository/branches")
    branch.save_query()
    branch_list = []
    for item in branch.run_query():
        name = item['name']
        if name != 'master':
            branch_list.append(name)
    assert_equal(len(branch_list), 20)
    # assert_equal(len(branch_list), 20)
