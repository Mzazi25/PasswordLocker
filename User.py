class User:
    """
    Created a class that generates new instances for Users
    """
    user_list = [] #Empty Array to Store Users

    def __init__(self,user_name,user_password):
        """
        def_init to define user_names and user_passwords
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

    @classmethod
    def find_by_user(cls,user_name):
        """
        Method that takes in a string and returns the user's details that matches the account
        """
        for user in cls.user_list:
            if user.user_name == user_name:
                return user

    @classmethod
    def user_exist(cls,user_name,user_password):
        """
        user_exists takes in a string and finds if the user being searched exists.
        """
        for user in cls.user_list:
            if user.username == user_name and user.userpassword==user_password:
                return True
        return False

