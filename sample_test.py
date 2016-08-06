import unittest
from bubble_sort import bubble_sort


class TestBubbleSortMethod(unittest.TestCase):

    def test_pos(self):
        self.assertTrue(bubble_sort([1,2,3,4,5]), [1,2,3,4,5])
        
    def test_pos_with_zero(self):
        self.assertTrue(bubble_sort([5,1,2,30,4,5]), [1,2,4,5,5,30])
    
    def test_neg(self):
        self.assertEqual(bubble_sort([-5, -1,-2, -30, -4, -5]), [ -30, -5, -5, -4, -2, -1])        
    
    def test_neg_with_zero(self):
        self.assertEqual(bubble_sort([-5, -1,-2, 0, -30, -4, -5]), [ -30, -5, -5, -4, -2, -1, 0])        
  
    def test_null(self):
        self.assertEqual(bubble_sort([]), [])
    
    def test_zeros(self):
        self.assertEqual(bubble_sort([0,0,0,0]), [0,0,0,0])            
 
	
if __name__ == '__main__':
    unittest.main()
