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