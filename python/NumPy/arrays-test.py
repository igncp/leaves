import unittest
import numpy as np

arr1 = np.array([[1,2], [3,4], [5,6]])
arr2 = np.array([[1,2],[3,2]])
arr3 = np.zeros((1,2,3))
arr4 = np.eye(10) # same as identity
arr5 = np.arange(4)

class ArraysTestCase(unittest.TestCase):
  def shape_test(self):
    self.assertEquals(arr1.shape, (3,2))
    self.assertEquals(arr2.shape, (2,2))
    self.assertEquals(arr3.shape, (1,2,3))
    self.assertEquals(arr4.shape, (10,10))
    self.assertEquals(arr5.shape, (4,))
  
  def dimension_test(self):
    self.assertEquals(arr1.ndim, 2)
    self.assertEquals(arr2.ndim, 2)
    self.assertEquals(arr3.ndim, 3)
    self.assertEquals(arr4.ndim, 2)
    self.assertEquals(arr4.ndim, 2)

  def operations_test(self):
    self.assertEquals(type(arr2), np.ndarray)
    self.assertEquals(type(np.dot(arr2, arr2)), np.ndarray)
    np.testing.assert_array_equal(np.dot(arr2, np.eye(2)), arr2)