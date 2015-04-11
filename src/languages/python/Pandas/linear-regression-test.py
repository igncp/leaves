# -*- coding: utf-8 -*-
# Inspired in: Justin Duke - http://jmduke.com/posts/basic-linear-regressions-in-python/

import unittest
import pandas as pd
import numpy as np
import random as rd
import matplotlib.pyplot as plt
import os

# Generate dataset (y = a·x + b)
data = []
a = rd.randint(1, 10)
b = rd.randint(-100, 100)

for i in np.arange(1000):
  val = i * a + b * rd.randint(0, 10) + rd.uniform(-1, 1) * 10
  data.append(val)

data = pd.Series(data)

# Calculate linear regression
a0, b0 = np.polyfit(data.index, data, 1)


class LinearRegressionTestCase(unittest.TestCase):
  def calculated_values_are_similar_test(self):
    self.assertTrue(abs(a - a0) < abs(2 * a))
    self.assertTrue(abs(b0) < abs(b * 10))
    # Generate plot of dataset and regression result
    if os.environ['LEAVES_PYTHON_WITH_PLOTS'] == 'true':
      linear_regression = []
      for i in np.arange(1000):
        linear_regression.append(a0 * i + b0)
      linear_regression = pd.Series(linear_regression)
      
      plt.plot(data, 'o', ms=2)
      plt.plot(linear_regression, 'r')
      plt.title('Linear Regression Example')
      plt.tight_layout()
      filepath = 'reports/languages/python/linear-regression.png'
      plt.savefig(filepath)
      plt.close()
