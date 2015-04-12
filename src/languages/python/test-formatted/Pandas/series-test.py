import unittest
import pandas as pd
import numpy as np
from pandas import Series

# Using parts of Python for Data Analysis - Wes McKinney

ser1 = Series([1, 4, 6, 8])
ser2 = Series([1, 6, -1, 2, None], index=['g', 'r', 'a', 'z', 'u'])


class SeriesTestCase(unittest.TestCase):
  def using_series_test(self):
    self.assertIsInstance(ser1.values, np.ndarray)
    self.assertEquals(len(ser1[ser1 < 0]), 0)
    self.assertEquals(len(ser1[ser1 > 0]), 4)
    self.assertTrue('g' in ser2)
    self.assertFalse('f' in ser2)
    self.assertFalse('f' in ser2)
    self.assertTrue(pd.notnull(ser2)['g'])
    self.assertFalse(pd.notnull(ser2)['u'])
