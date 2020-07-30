import requests

headers = {"Authorization": "Bearer Gh9kuLv9dc3_aYsjoT-6"}


def run_query(query):
    request = requests.post('https://gitlab.com/api/graphql',
                            json={'query': query},
                            headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception(
            "Query failed to run by returning code of {}. {}".format(
                request.status_code, query))


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

result = run_query(query)
print(result)
