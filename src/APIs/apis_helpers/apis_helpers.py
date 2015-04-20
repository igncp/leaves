import yaml
import os
import sys


def get_credentials(api_name):
  file_path = 'config/APIs/' + api_name + '/credentials.yml'
  if not os.path.isfile(file_path):
    print 'The credentials file does not exist at: ' + file_path
    sys.exit()
  data = open(file_path, 'r')
  parsed_data = yaml.load(data)
  return parsed_data
