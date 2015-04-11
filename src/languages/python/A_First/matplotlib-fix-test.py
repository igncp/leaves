# This dummy test fixes a matplotlib issue inside a headless VM

import unittest
import matplotlib
matplotlib.use('Agg')


class ArraysTestCase(unittest.TestCase):
  def shape_test(self):
    self.assertEquals(1, 1)
