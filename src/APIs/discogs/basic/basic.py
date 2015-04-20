import os, sys
inserted_path = '/../discogs_helpers/'
sys.path.insert(0, os.path.realpath(os.path.dirname(__file__) + inserted_path))
from termcolor import colored as clrd
import discogs_helpers
from pandas import DataFrame
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns


def generate_bar_plot(data):
  def autolabel(ax, bars):
    for rect in bars:
      height = rect.get_height()
      ax.text(rect.get_x() + rect.get_width() / 2., height + 0.5, str(height),
        ha='center')

  sorted_data = data.sort(columns=['year'])
  years = sorted_data['year']
  ind = np.arange(len(years))
  width = 0.3
  colors = sns.color_palette("cubehelix", 8)
  fig, ax = plt.subplots()
  bars = plt.bar(ind, years, width, alpha=0.7, color=colors)
  plt.ylabel("Year")
  plt.ylim([years.min() - 2, years.max() + 2])
  locs, labels = plt.xticks()
  plt.xticks(ind + width / 2., sorted_data['title'], rotation=45)
  plt.xlabel("Album")
  plt.title('Albums years')
  autolabel(ax, bars)
  plt.tight_layout()
  filepath = 'reports/APIs/discogs'
  if not os.path.isdir(filepath): os.makedirs(filepath)
  filepath += '/years.png'
  plt.savefig(filepath)
  plt.close()
  print 'A chart was created at ' + clrd(filepath, 'green')


def Main():
  max_length = 20
  discogs = discogs_helpers.authenticate()
  keywords = raw_input('Type some keyworks to search by: ')
  if keywords is '':
    keywords = 'Big Star'
    print 'No keywords were typed. Using "{}" by default.'.format(keywords)
  results = discogs.search(keywords, type='release')
  print 'Number of results: ' + clrd(str(results.count), 'green')
  if results.count > max_length:
    releases = DataFrame(columns=['release', 'title', 'artists', 'year'])
    for num in range(max_length):
      release = results[num]
      artists = ', '.join([artist.name for artist in release.artists])
      releases.loc[num] = [release.id, release.title, artists, release.year]
    generate_bar_plot(releases)
  else:
    print 'As there are less than 10 results, nothing will be done.'
  
if __name__ == "__main__":
  Main()
