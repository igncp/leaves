import os, sys
import yaml
from termcolor import colored as clrd


def get_credentials(api_name):
  file_path = 'config/APIs/' + api_name + '/credentials.yml'
  if not os.path.isfile(file_path):
    print 'The credentials file does not exist at: ' + file_path
    sys.exit()
  data = open(file_path, 'r')
  parsed_data = yaml.load(data)
  return parsed_data


def save_fig(plt, directory, name):
  filepath = 'reports/APIs/' + directory
  if not os.path.isdir(filepath): os.makedirs(filepath)
  filepath += '/' + name + '.png'
  plt.savefig(filepath)
  print 'A chart was created at ' + clrd(filepath, 'green')
