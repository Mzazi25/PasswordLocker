class User:
    """
    Created a class that generates new instances for Users
    """
    user_list = [] #Empty Array to Store Users

    def __init__(self,username,userpassword):
        """
        def_init to define user_names and user_passwords
        """
        self.username = username
        self.userpassword = userpassword
    
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
    def find_by_user(cls,username):
        """
        Method that takes in a string and returns the user's details that matches the account
        """
        for user in cls.user_list:
            if user.username ==username:
                return user

    @classmethod
    def user_exist(cls,username):
        """
        user_exists takes in a string and finds if the user being searched exists.
        """
        for user in cls.user_list:

            if user.username == username:
                return user

    @classmethod
    def display_user(cls):
        """
        Added method to display users
        """
        return cls.user_list