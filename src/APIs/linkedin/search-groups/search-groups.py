import yaml
import json
import random
from linkedin import linkedin
from pandas import Series
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def Authentication():
  credentials = open('config/APIs/linkedin/credentials.yml', 'r')
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


def getWordsPercentages(strings_list):
  words = [item for sublist in strings_list for item in sublist] # Flatten list
  words = [word for word in words if len(word) > 3] # Remove short words
  words = [word.lower() for word in words]
  words = Series(words)
  num_percentages = (words.value_counts() / len(words) * 100)
  percentages = num_percentages.map('{:,.2f} %'.format)
  return percentages, len(percentages), num_percentages


def generateBarPlot(percentages, title):
  ind = np.arange(len(percentages))
  width = 0.3
  colors = sns.color_palette("cubehelix", 8)
  plt.bar(ind, percentages, width, alpha=0.7, color=colors)
  plt.xticks(ind+width/2., percentages.index, rotation=45)
  locs, labels = plt.yticks()
  plt.yticks(locs, map(lambda x: "%.2f" % x + ' %', locs))
  plt.ylabel("Percentage")
  plt.xlabel("Word")
  plt.title(title)
  plt.tight_layout()
  filepath = 'plots/apis/linkedin/search_groups.png'
  plt.savefig(filepath)
  plt.close()
  print 'A chart was created at ' + filepath


def AnalyzeGroup(app, group):
  posts = app.get_posts(group['_key'], params={'count': 100})['values']
  titles = [post['title'].split() for post in posts]
  percentages, total, num_percentages = getWordsPercentages(titles)

  print 'Top 10 big word repetition in titles of posts percentage (of a total of {0}):'.format(total)
  print percentages.head(10)
  generateBarPlot(num_percentages.head(20), group['group']['name'])

  creators_headlines = [post['creator']['headline'].split() for post in posts if 'headline' in post['creator']]
  percentages, total, num_percentages = getWordsPercentages(creators_headlines)
  
  print 'Top 10 big word repetition in headlines of creators of posts percentage (of a total of {0}):'.format(total)
  print percentages.head(10)


if __name__ == "__main__":
  Main()
