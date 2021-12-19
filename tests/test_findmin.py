import unittest
from findmin import monotonic, findmin

class testFindmin(unittest.TestCase):
    def test_findmin(self):
        #write test pull up assert methods 
        with self.assertRaises(ValueError):
            findmin([-2,-1,0,1,2,3])
        with self.assertRaises(ValueError):
            findmin([-2,-1,0,3,2,1])
        with self.assertRaises(ValueError):
            findmin([1,2,0,1,2,3])
        with self.assertRaises(ValueError):
            findmin([1,2,-1,-2,1])
        with self.assertRaises(ValueError):
            findmin([])

        self.assertEqual(findmin([3,1,0,1,2,3]),0)
        self.assertEqual(findmin([3,2,1,3,5]),1)
        self.assertEqual(findmin([3,2,1,0,-3,-2,-1]),-3)

    
    def test_monotonic(self):
        #write test pull up assert methods 

        #True Corner cases
        self.assertEqual(monotonic([3,1,0,1,2,3]),True)
        self.assertEqual(monotonic([3,2,1,3,5]),True)
        self.assertEqual(monotonic([3,2,1,0,-3,-2,-1]),True)
        self.assertEqual(monotonic(['z','y','x','a','b','c','d']),True)

        #False Corner cases
        self.assertEqual(monotonic([]),False)
        self.assertEqual(monotonic([1]),False)
        self.assertEqual(monotonic([-1]),False)
        self.assertEqual(monotonic([1,3,2]),False)
        self.assertEqual(monotonic([3,2,1]),False)
        self.assertEqual(monotonic([-2,-1,0,1,2,3]),False) 
        self.assertEqual(monotonic([2,1,1,2,3]),False) #Test Duplicates


if __name__ == '__main__':
    unittest.main()