import yaml
from linkedin import linkedin
from pandas import Series


def Main():
  credentials = open('apis/linkedin/credentials/credentials.yml', 'r')
  cs = yaml.load(credentials)
  authentication = linkedin.LinkedInDeveloperAuthentication(cs['consumer-key'],
    cs['consumer-secret'], cs['user-token'], cs['user-secret'],
    cs['return-url'], linkedin.PERMISSIONS.enums.values())
  application = linkedin.LinkedInApplication(authentication)
  profile = application.get_profile()
  print 'The account\'s owner name is ' + profile['firstName'] + ' ' + profile['lastName']


if __name__ == "__main__":
  Main()
