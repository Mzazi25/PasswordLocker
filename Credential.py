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