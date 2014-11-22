import csv
import urllib2
import numpy as np
from pandas import DataFrame
import matplotlib.pyplot as pl


def Main():
  companies = ['AAPL', 'ADSK', 'GOOG', 'MSFT', 'AUY', 'TWTR', 'YHOO', 'CAT', 'GE', 'CSCO', 'F']
  url = 'http://finance.yahoo.com/d/quotes.csv?s=' + '+'.join(companies) + '&f=nabp'
  response = urllib2.urlopen(url)
  data = list(csv.reader(response))
  columns = ['Name', 'Pricing - Ask', 'Pricing - Bid', 'Previous close']
  data = DataFrame(data, columns=columns)
  data = data.replace(['N/A'], [0])
  data['Previous close'] = data['Previous close'].astype(float)
  data = data.sort(columns=['Previous close'], ascending=False, axis=0)

  # Create plot
  pl.plot(data['Pricing - Ask'], label='Pricing Ask')
  pl.plot(data['Pricing - Bid'], label='Pricing Bid')
  pl.plot(data['Previous close'], label='Previous Close')
  pl.title("Stock values for some companies (Sorted by Ask)")
  pl.xticks(np.arange(len(data['Name'])), data['Name'].tolist(), rotation=45)
  pl.legend()
  pl.tight_layout()
  filepath = 'plots/apis/yahoo_finance/basic.png'
  pl.savefig(filepath)
  pl.close()
  print 'A chart was created at ' + filepath


if __name__ == "__main__":
  Main()
