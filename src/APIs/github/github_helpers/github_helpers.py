from github import Github
import os, sys
sys.path.insert(0, os.path.realpath(os.path.dirname(__file__) + '../../../apis_helpers'))
import apis_helpers


def authenticate():
  credentials = apis_helpers.get_credentials('github')
  ACCESS_TOKEN = credentials['access-token']
  client = Github(ACCESS_TOKEN, per_page=100)
  return client
