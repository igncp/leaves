import yaml
from github import Github
from pandas import Series


def Main():
  credentials = open('apis/github/credentials/credentials.yml', 'r')
  credentials = yaml.load(credentials)
  ACCESS_TOKEN = credentials['access-token']
  client = Github(ACCESS_TOKEN, per_page=100)
  username = raw_input("Please, enter a user name: ")
  user = client.get_user(username)

  print 'The user\'s displayed name is ' + user.name


if __name__ == "__main__":
  Main()
