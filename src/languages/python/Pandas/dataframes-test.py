# -*- coding: utf-8 -*-

# Pandas has a Panel data structure, which you can think of as a
# three-dimensional analogue of DataFrame

import unittest
from pandas import DataFrame

data = {'state': ['Madrid', 'Cataluña', 'Aragón', 'Castilla y León'],
  'year': [2000, 2001, 2002, 2001], 'pop': [1.5, 1.7, 3.6, 2.4]}
frame = DataFrame(data)


class DataFramesTestCase(unittest.TestCase):
  def using_dataframes_test(self):
    self.assertIn('state', frame)
    self.assertEquals(len(frame.index), 4)
