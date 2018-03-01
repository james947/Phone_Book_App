import unittest
from phone import Phone

class PhoneTestCase(unittest.TestCase):
    #tests if number is added 
    def test_add_new_number(self):
        new = Phone()
        response=new.add_new(name="james",number=555)
        self.assertEqual(response['message'], "Business added succesfully")

    def test_delete_contact(self):
        new = Phone()
        response=new.add_new(name="james",number=555)
        response=new.delete(name="james")
        self.assertEqual(response['message'], "Contact deleted succesfully")

    def test_view_contacts(self):
        new=Phone()
        response=new.add_new(name="james",number=555)
        response=new.view_contacts()
        self.assertEqual(response,{'number': 555, 'name': 'james'})

    def test_update_contacts(self):
        new=Phone()
        response=new.add_new(name="james",number=555)
        response=new.update_contacts(name="ken",number=222)
        self.assertEqual(response['message'], "Contact updated succesfully")
        





if __name__ == '__main__':
    unittest.main()