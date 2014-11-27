import yaml
import json
import random
from linkedin import linkedin
from pandas import Series


def Authentication():
  credentials = open('apis/linkedin/credentials/credentials.yml', 'r')
  cs = yaml.load(credentials)
  authentication = linkedin.LinkedInDeveloperAuthentication(cs['consumer-key'],
    cs['consumer-secret'], cs['user-token'], cs['user-secret'],
    cs['return-url'], linkedin.PERMISSIONS.enums.values())
  return linkedin.LinkedInApplication(authentication)


def Main():
  app = Authentication()
  groups = app.get_memberships(params={'count': 100})
  if groups['_total'] > 0:
    if '_count' in groups:
      selected = random.randint(0,groups['_count'] - 1)
    else:
      selected = random.randint(0,groups['_total'] - 1)

    print "You're subscribed to " + str(groups['_total']) + " groups."
    print "The last posts of the '" + str(groups['values'][selected]['group']['name']) + \
      "' group (randomly selected) will be analyzed."
    AnalyzeGroup(app, groups['values'][selected])
  else:
    print "You aren't in any group. This ends here."


def AnalyzeGroup(app, group):
  posts = app.get_posts(group['_key'], params={'count': 100})['values']
  titles = [post['title'].split() for post in posts]
  words = [item for sublist in titles for item in sublist] # Flatten list
  words = [word.lower() for word in words]
  words = Series(words)
  percentages = (words.value_counts() / len(words) * 100).map('{:,.2f} %'.format)

  print 'Top 10 word repetition in titles of posts percentage (of a total of {0}):'.format(len(words))
  print percentages.head(10)


if __name__ == "__main__":
  Main()
