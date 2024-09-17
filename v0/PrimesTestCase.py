import unittest 
from prime import is_prime 

class PrimesTestCase(unittest.TestCase):
   def test_is_five_prime(self):    
      self.assertTrue(is_prime(5)) 
	   
   #<Include your test here>
   def test_is_seven_prime(self):    
      self.assertTrue(is_prime(7)) 

   def test_is_twentyfive_prime(self):    
      self.assertTrue(is_prime(25)) 

   def test_is_one_prime(self):
	   self.assertTrue(is_prime(1))



   

   

if __name__ == '__main__':
	unittest.main()
