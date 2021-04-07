import requests
import os
import sys
from pathlib import Path

print("Running" if __name__ == "__main__" else "Importing", Path(__file__).resolve())

# if __name__ == "__main__":
#     import api
# else:
#     from . import api

# try:
#     from pol import api
# except ImportError:
#     print("ImportError")
#     print("Try import api")
#     import api

current_folder = Path(__file__).absolute().parent
father_folder = str(current_folder.parent)
sys.path.append(father_folder)

from pol import api


def ch1():
    branch = api.QueryREST(
        "101camp9py-branch",
        "https://gitlab.com/api/v4/projects/18907382/repository/branches",
    )
    branch.save_query()

    branch_list = []
    for item in branch.run_query():
        name = item["name"]
        if name != "master":
            branch_list.append(name)
    for branch_name in branch_list:
        print(branch_name)
    print("\nThe number of branches is {}.".format(len(branch_list)))


def ch2():
    issue = api.QueryGraphQL(
        "101camp9py-issue-001-100",
        """
    {
        project(fullPath: "101camp/9py/tasks") {
            id
            name
            description
            issues(createdBefore: "2020-07-12T04:42:56Z") {
            nodes {
                title
                id
                iid
                createdAt
                userNotesCount
                author {
                id
                name
                }
                notes{
                nodes {
                    id
                    author {
                    id
                    name
                    }
                    createdAt
                    body
                }
                }
            }
            }
        }
    }
    """,
        {},
    )
    issue.save_query()  # print(type(issue.run_query()))


if __name__ == "__main__":
    ch1()
    ch2()
