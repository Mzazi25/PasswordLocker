from credential import Credential
from user import User
import unittest

class TestCredentialandUser(unittest.TestCase):
    def tearDown(self):
        """
        tearDown methods cleans up after each test cas has run
        """
        Credential.credential_list = []
        User.user_list =[]
    
    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.new_user= User("Caleb","Langat90")
        self.new_credential= Credential("Twitter","Mzazi","Langat25")
    
    def test_init(self):

        """
        test_init method to test if the object is initialized well
        """
        self.assertEqual(self.new_user.user_name,"Caleb")
        self.assertEqual(self.new_user.user_password,"Langat90")
        self.assertEqual(self.new_credential.app_name,"Twitter")
        self.assertEqual(self.new_credential.credential_user_name,"Mzazi")
        self.assertEqual(self.new_credential.credential_password,"Langat25")


