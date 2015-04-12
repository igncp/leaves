import unittest
import numpy as np
import matplotlib.pyplot as pl
import random
import os

# Using parts of Python for Data Analysis - Wes McKinney


class RandomTestCase(unittest.TestCase):
  def random_direction_test(self):
    position = 0
    walk = [position]
    steps = 1000

    for i in xrange(steps):
      step = 1 if random.randint(0, 1) else -1
      position += step
      walk.append(position)
    self.assertIsInstance(position, int)
    # It is `relative` safe to consider negligible the possibility of all 0
    self.assertTrue(np.min(walk) < np.max(walk))
    if os.environ['LEAVES_PYTHON_WITH_PLOTS'] == 'true':
      pl.plot(walk)
      pl.title("Random position change for 1000 steps")
      pl.ylabel('Position')
      pl.xlabel('Steps')
      filepath = 'reports/languages/python/'
      if not os.path.isdir(filepath): os.makedirs(filepath)
      pl.savefig(filepath + "random-direction.png")
      pl.close()
