import yaml
import json
from github import Github
import pandas as pd
import numpy as np

def Main():
  credentials = open('apis/github/credentials/credentials.yml', 'r')
  credentials = yaml.load(credentials)
  ACCESS_TOKEN = credentials['access-token']
  client = Github(ACCESS_TOKEN, per_page=100)
  keywords = raw_input("Please, enter keywords to search repositories: ")
  search = client.search_repositories(keywords)
  print 'Total count: ' + str(search.totalCount)

if __name__ == "__main__":
  Main()
