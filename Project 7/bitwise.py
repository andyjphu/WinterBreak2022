import unittest 
'''
class testAny(unittest.TestCase):
    def testBitWise(self):
        for i in range(3355443):
            self.assertEqual(512,2<<8)
            
'''
class testEx(unittest.TestCase):
    def testNormal(self):
        for i in range(3355443):
            self.assertEqual(512, 2**9)
      
unittest.main()