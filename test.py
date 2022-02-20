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
    
