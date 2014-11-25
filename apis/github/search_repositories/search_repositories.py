import yaml
from github import Github
from pandas import Series


def Main():
  credentials = open('apis/github/credentials/credentials.yml', 'r')
  credentials = yaml.load(credentials)
  ACCESS_TOKEN = credentials['access-token']
  client = Github(ACCESS_TOKEN, per_page=100)
  keywords = raw_input("Please, enter keywords to search repositories: ")
  search = client.search_repositories(keywords)
  first_page = search.get_page(0)

  languages = Series(r.language for r in first_page)
  languages = languages.dropna()
  languages.sort()

  print 'Languages percentage:'
  print languages.value_counts() / len(languages) * 100


if __name__ == "__main__":
  Main()
