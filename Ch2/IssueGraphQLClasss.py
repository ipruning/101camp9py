import requests


class QueryGraphQL(object):
    def __init__(self, query, variables):
        super(QueryGraphQL, self).__init__()
        self.query = query
        self.variables = variables
        self.headers = {"Authorization": "Bearer Gh9kuLv9dc3_aYsjoT-6"}

    """docstring for graphQL"""
    def run_query(
            self, query, variables
    ):  # A simple function to use requests.post to make the API call. Note the json= section.
        request = requests.post('https://gitlab.com/api/graphql',
                                json={
                                    'query': query,
                                    'variables': variables
                                },
                                headers=self.headers)
        if request.status_code == 200:
            return request.json()
        else:
            raise Exception(
                "Query failed to run by returning code of {}. {}".format(
                    request.status_code, query))

    def get_query(self):
        result = self.run_query(self.query, self.variables)  #execute query
        print(result)


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

variables = {}

Issue = QueryGraphQL(query, variables)
Issue.get_query()
