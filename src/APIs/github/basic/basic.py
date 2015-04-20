import os, sys
sys.path.insert(0, os.path.realpath(os.path.dirname(__file__) + '/../github_helpers/'))
import github_helpers


def Main():
  client = github_helpers.authenticate()
  username = raw_input("Please, enter a user name: ")
  user = client.get_user(username)

  print "The user's displayed name is " + user.name


if __name__ == "__main__":
  Main()
