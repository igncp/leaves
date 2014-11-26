import yaml
from github import Github
from pandas import Series
import matplotlib.pyplot as pl
import numpy as np


def Main():
  credentials = open('apis/github/credentials/credentials.yml', 'r')
  credentials = yaml.load(credentials)
  ACCESS_TOKEN = credentials['access-token']
  client = Github(ACCESS_TOKEN, per_page=100)
  keywords = raw_input("Please, enter keywords to search repositories: ")
  search = client.search_repositories(keywords)
  first_page = search.get_page(0)

  languages = Series(r.language for r in first_page)
  languages = languages.dropna()
  languages.sort()

  percentages = (languages.value_counts() / len(languages) * 100).map('{:,.2f} %'.format)

  print 'Languages percentage:'
  print percentages

  # Create plot
  x = [int(r.stargazers_count) for r in first_page]
  y = [int(r.forks) for r in first_page]

  # Add one to every value for logarithmic scale
  x = [val + 1 for val in x]
  y = [val + 1 for val in y]

  area = [100 for r in first_page]
  names = [r.name for r in first_page]
  colors = np.random.rand(len(first_page))
  pl.scatter(x, y, s=area, c=colors, alpha=0.5)
  for i in range(0, len(x)):
    pl.annotate(names[i], (x[i], y[i]), fontsize=2)
  pl.title("All values are with addition of 1 (for the logarithmic scale)")
  pl.xlabel("Stars")
  pl.xscale("log")
  pl.yscale("log")
  pl.ylabel("Forks")
  pl.tight_layout()
  filepath = 'plots/apis/github/search_repositories.png'
  pl.savefig(filepath, figsize=(1020, 1020), dpi=300)
  pl.close()
  print 'A chart with high resolution and small font size (to minimize overlaps) was created at ' + filepath

if __name__ == "__main__":
  Main()
