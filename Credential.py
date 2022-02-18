from operator import truediv


class Credential:
    """
    Added Crediatial class
    """
    credential_list=[] #Empty Array to append creditials

    def __init__(self,credential_name, credential_password):
        """
        def_init to define credential_names and credential_passwords
        """
        self.credential_name= credential_name
        self.credential_password= credential_password

    def save_credential(self):
        """
        save credential details to the credential_list
        """
        Credential.credential_list.append(self)
    
    def delete_credential(self):
        """
        save credential details to the credential_list
        """
        Credential.credential_list.remove(self)

    @classmethod
    def find_by_credential(cls,string):
        """
        Method that takes in a string and returns the credential details that matches the account
        """
        for credential in cls.credential_list:
            if credential.credential_name == string:
                return credential

    @classmethod
    def credential_exists(cls,string):
        """
        Method that takes in a string and returns a boolian if the credential exists
        """
        for credential in cls.credential_list:
            if credential.credential_name == string:
                return True
        return False

    
