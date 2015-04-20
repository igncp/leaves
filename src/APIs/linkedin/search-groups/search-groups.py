from termcolor import colored as clrd
import random
import os
import sys
from pandas import Series
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

inserted_path = '/../linkedin_helpers'
sys.path.insert(0, os.path.realpath(os.path.dirname(__file__) + inserted_path))
import linkedin_helpers


def Main():
  app = linkedin_helpers.authenticate()
  groups = app.get_memberships(params={'count': 100})
  if groups['_total'] > 0:
    selected = random.randint(0, groups['_total'] - 1)

    print "You're subscribed to " + clrd(groups['_total'], 'green') + " groups."
    print "The last posts of the " + clrd(groups['values'][selected]['group']['name'], 'blue') + \
      " group (randomly selected) will be analyzed."
    analyze_group(app, groups['values'][selected])
  else:
    print "You aren't in any group. This ends here."


def get_words_percentages(strings_list):
  words = [item for sublist in strings_list for item in sublist] # Flatten list
  words = [word for word in words if len(word) > 3] # Remove short words
  words = [word.lower() for word in words]
  words = Series(words)
  num_percentages = 100.0 * words.value_counts() / len(words)
  percentages = num_percentages.map('{:,.2f} %'.format)
  return percentages, len(percentages), num_percentages


def generate_bar_plot(percentages, title):
  ind = np.arange(len(percentages))
  width = 0.3
  colors = sns.color_palette("cubehelix", 8)
  plt.bar(ind, percentages, width, alpha=0.7, color=colors)
  plt.xticks(ind + width / 2., percentages.index, rotation=45)
  locs, labels = plt.yticks()
  plt.yticks(locs, map(lambda x: "%.2f" % x + ' %', locs))
  plt.ylabel("Percentage")
  plt.xlabel("Word")
  plt.title(title)
  plt.tight_layout()
  filepath = 'reports/APIs/linkedin'
  if not os.path.isdir(filepath): os.makedirs(filepath)
  filepath += '/search_groups.png'
  plt.savefig(filepath)
  plt.close()
  print 'A chart was created at ' + clrd(filepath, 'green')


def analyze_group(app, group):
  posts = app.get_posts(group['_key'], params={'count': 100})['values']
  titles = [post['title'].split() for post in posts]
  percentages, total, num_percentages = get_words_percentages(titles)

  print 'Top 10 big word repetition in titles of posts percentage ' +\
    '(of a total of {0}):'.format(total)
  print percentages.head(10)
  generate_bar_plot(num_percentages.head(20), group['group']['name'])

  creators_headlines = [post['creator']['headline'].split() for post in posts
    if 'headline' in post['creator']]
  percentages, total, num_percentages = get_words_percentages(creators_headlines)
  
  print 'Top 10 big word repetition in headlines of creators of posts ' +\
    'percentage (of a total of {0}):'.format(total)

  print percentages.head(10)


if __name__ == "__main__":
  Main()
