from linkedin import linkedin
import os, sys
sys.path.insert(0, os.path.realpath(os.path.dirname(__file__) + '../../../apis_helpers'))
import apis_helpers


def get_credentials():
  return apis_helpers.get_credentials('linkedin')


def authenticate():
  credentials = get_credentials()
  authentication = linkedin.LinkedInDeveloperAuthentication(credentials['consumer-key'],
    credentials['consumer-secret'], credentials['user-token'], credentials['user-secret'],
    credentials['return-url'], linkedin.PERMISSIONS.enums.values())
  return linkedin.LinkedInApplication(authentication)


def save_fig(plt, name):
  apis_helpers.save_fig(plt, 'linkedin', name)
