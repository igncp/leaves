import yaml
from linkedin import linkedin


def Main():
  credentials = open('config/APIs/linkedin/credentials.yml', 'r')
  cs = yaml.load(credentials)
  authentication = linkedin.LinkedInDeveloperAuthentication(cs['consumer-key'],
    cs['consumer-secret'], cs['user-token'], cs['user-secret'],
    cs['return-url'], linkedin.PERMISSIONS.enums.values())
  application = linkedin.LinkedInApplication(authentication)
  profile = application.get_profile()
  message = "The account's owner name is {} {}".format(profile['firstName'], profile['lastName'])
  print message


if __name__ == "__main__":
  Main()
