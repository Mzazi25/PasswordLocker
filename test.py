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

    def test_save_user(self):
        """
        test_save_user method checks if the users objects is saved into the user_list
        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def test_save_credential(self):
        """
        test_save_user method checks if the credential objects is saved into the credential_list
        """
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),1)

    def test_save_multiple_user(self):
        """
        test_save_multiple_user to check if we can save multiple user
        objects to our user_list
        """
        self.new_user.save_user()
        test_user = User("Test","user") # new user
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)
    
    def test_save_multiple_credential(self):
        """
        test_save_multiple_credentials to check if we can save multiple credentials objects to our credential_list
        """
        self.new_credential.save_credential()
        test_credential = Credential("Instagram","Test","user") # new user
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),2)

    def test_delete_User(self):
            """
            test_delete_user to test if we can remove a user from our user list
            """
            self.new_user.save_user()
            test_user = User("Test","user") # new user
            test_user.save_user()

            self.new_user.delete_user()# Deleting a user object
            self.assertEqual(len(User.user_list),1)

    def test_delete_User(self):

        """
        test_delete_user to test if we can remove a user from our user list
        """
        self.new_user.save_user()
        test_user = User("Test","user") # new user
        test_user.save_user()

        self.new_user.delete_user()# Deleting a user object
        self.assertEqual(len(User.user_list),1)

    def test_delete_Credential(self):

        """
        test_delete_credential to test if we can remove a credential from our credential list
        """
        self.new_credential.save_credential()
        test_credential = Credential("Twitter","Test","user") # new credential
        test_credential.save_credential()

        self.new_credential.delete_credential()# Deleting a credential object
        self.assertEqual(len(Credential.credential_list),1)


       


