from pol import api
import requests

# Ch1

branch = api.QueryREST(
    "101camp9py-branch",
    "https://gitlab.com/api/v4/projects/18907382/repository/branches")
branch.save_query()

branch_list = []
for item in branch.run_query():
    name = item['name']
    if name != 'master':
        branch_list.append(name)
for branch_name in branch_list:
    print(branch_name)
print('\nThe number of branches is {}.'.format(len(branch_list)))

# Ch2

query = """
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
"""

issue = api.QueryGraphQL("101camp9py-issue-001-100", query, {})
issue.save_query()
# print(type(issue.run_query()))
