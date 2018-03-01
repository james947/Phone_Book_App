import unittest
from phone import Phone

class PhoneTestCase(unittest.TestCase):
    #tests if number is added 
    def test_add_new_number(self):
        new = Phone()
        response=new.add_new(name="james",number=555)
        self.assertEqual(response['message'], "Business added succesfully")

 



if __name__ == '__main__':
    unittest.main()