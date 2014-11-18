import unittest
import numpy as np
import matplotlib.pyplot as pl
import math

# Using parts of Python for Data Analysis - Wes McKinney

arr1 = np.array([[1,2], [3,4], [5,6]])
arr2 = np.array([[1,2],[3,2]])
arr3 = np.zeros((1,2,3))
arr4 = np.eye(10) # same as identity
arr5 = np.arange(4)
arr6 = np.random.randn(2, 4, 3)

class ArraysTestCase(unittest.TestCase):
  def shape_test(self):
    self.assertEquals(arr1.shape, (3,2))
    self.assertEquals(arr1.T.shape, (2,3))
    self.assertEquals(arr2.shape, (2,2))
    self.assertEquals(arr3.shape, (1,2,3))
    self.assertEquals(arr4.shape, (10,10))
    self.assertEquals(arr5.shape, (4,))
    self.assertEquals(arr6[1:, :2, :1].shape, (1,2,1))
  
  def dimension_test(self):
    self.assertEquals(arr1.ndim, 2)
    self.assertEquals(arr2.ndim, 2)
    self.assertEquals(arr3.ndim, 3)
    self.assertEquals(arr4.ndim, 2)
    self.assertEquals(arr5.ndim, 1)
    self.assertEquals(arr6.ndim, 3)

  def indexing_test(self):
    np.testing.assert_array_equal(arr1[0], [1,2])
    self.assertEquals(arr1[1][0], 3)
    np.testing.assert_array_equal(arr3[0], np.zeros((2,3)))
    self.assertEquals(len(arr4[0]), 10)
  
  def operations_test(self):
    self.assertEquals(type(arr2), np.ndarray)
    self.assertEquals(type(np.dot(arr2, arr2)), np.ndarray)
    np.testing.assert_array_equal(np.dot(arr2, np.eye(2)), arr2)
  
  def universal_functions_test(self):
    np.testing.assert_array_equal(np.sqrt(arr5), [0,1,math.sqrt(2),math.sqrt(3)])
    np.testing.assert_array_equal(np.isinf(arr1), False)
    np.testing.assert_array_equal(np.ceil(arr1), arr1)
    np.testing.assert_array_equal(np.add(arr4, arr4), 2 * arr4)

  def mesh_test(self):
    points = np.arange(-10, 10, 0.01) # 2000 equally spaced points
    xs, ys = np.meshgrid(points, points) # 2 arrays of 2000x2000, second is transposed
    self.assertEquals(xs.shape, (2000,2000))
    self.assertEquals(round(xs[0][1000],2), 0.0) # Center
    self.assertEquals(round(xs[0][0],2), -10)
    # As it is transposed, all the row is equal
    self.assertEquals(round(ys[0][1000],2), -10)
    self.assertEquals(round(ys[0][0],2), -10)
    z = np.sqrt(xs ** 2 + ys ** 2)
    self.assertEquals(round(z[0][0],0), 14) # sqrt(200)
    self.assertEquals(round(z[1000][1000],0), 0)
    # Create plot
    pl.imshow(z, cmap=pl.cm.Blues)
    pl.colorbar()
    pl.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
    pl.savefig("plots/python/mesh.png")
    pl.close()