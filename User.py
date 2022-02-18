from this import d


class User:
    """
    Created a class that generates new instances for Users
    """
    user_list = [] #Empty Array to Store Users

    def __init__(self,user_name,user_password):
        """
        Def_Init to define user_names and user_passwords
        """
        self.user_name=user_name
        self.user_password=user_password
    
    def save_user(self):
        """
        save user details to the user_list
        """
        User.user_list.append(self)

    def delete_user(self):
        """
        delete_user method deletes saved user from the contact_list
        """
        User.user_list.remove(self)