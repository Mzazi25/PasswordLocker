#!/usr/bin/env python3.9
from user import User
from credential import Credential
import string
import random

def create_user(username,userpassword):
    """
    Function to create User
    """
    new_user = User(username,userpassword),
    return new_user

def create_credential(app_name,credential_user_name,credential_password):
    """
    Function to create Credential
    """
    new_credential = Credential(app_name,credential_user_name,credential_password),
    return new_credential

def save_user(self):
    '''
    Function to save user
    '''
    User.save_user(self)

def save_credential(self):
    '''
    Function to save credential
    '''
    Credential.save_credential(self)

def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

def del_credential(credential):
    '''
    Function to delete credential
    '''
    credential.delete_credential()

def find_user(user):
    '''
    Function that finds a user by the username and returns the user details
    '''
    return User.find_by_user(user)

def find_credential(self):
    '''
    Function that finds the credentials from the app name
    '''
    return Credential.find_by_app(self)

def check_existing_user(username,userpassword):
    '''
    Function that check if a user exists and returns a Boolean
    '''
    return User.find_by_user(username,userpassword)
@classmethod
def password_gen(length):
    """
    generate random password
    """
    letters = string.ascii_lowercase
    result = ''.join((random.sample(letters, length)))  
    auto_gen_password= result
    return auto_gen_password

def check_existing_credential(app_name,credential_user_name,credential_password):
    '''
    Function that check if a credential exists and returns a Boolean
    '''
    return Credential.credential_exists(app_name,credential_user_name,credential_password)

def display_user():
    '''
    Function that returns all the saved users
    '''
    return User.display_user()

def display_credential():
    '''
    Function that returns all the saved credentials
    '''
    return Credential.display_credentials()

def main():
    print("Hello Welcome to your Password Locker. What is your name?")
    username = input()

    print(f"Hello {username}. what would you like to do?")
    print('\n')

    while True:
                print("Use these short codes : cc - create a new Account, si - Sign In Account , du- Delete User, ex -exit the contact list ")

                short_code = input().lower()

                if short_code == 'cc':
                       if short_code == 'cc':
                            print("New Account")
                            print("-"*10)

                            print ("Username ....")
                            username = input()

                            print("Password ...")
                            print(" "*4 + "*the password must be 6 characters or longer*")
                            print("Do you want your password Generated? Y/N")
                            generate_pass =input().upper()
                            if generate_pass == "Y":
                                password_length = int(input("What length would you like your password to be,i.e 6,8..."))
                                letters = string.ascii_lowercase
                                auto_gen_password = ("".join(random.choice(letters) for i in range(password_length)))
                                
                                print("\u001b[35;1mYour generated password is: \u001b[0m",auto_gen_password)
                                new_user_password = auto_gen_password
                                print("input your generate password to proceed")
                            else:
                                print("Input your password")


                            while True:
                                userpassword = input()
                                if len(userpassword) >=6:
                                    save_user(create_user(username,userpassword)) # create and save new contact.
                                    print ('\n')
                                    print(f"New Account {username} {userpassword} created proceed to Sign in")
                                    print ('\n')
                                    break
                                else:
                                    print("Password too short!")
                                    continue
                            
                        

                elif short_code == 'si':

                            print("Please sign in to the account")
                            print ("Username ....")
                            username = input()

                            print("Password ...")

                            print(" "*4 + "*the password must be 6 characters or longer*")
                            print("Do you want your password Generated? Y/N")
                            generate_pass =input().upper()
                            if generate_pass == "Y":
                                password_length = int(input("What length would you like your password to be,i.e 6,8..."))
                                letters = string.ascii_lowercase
                                auto_gen_password = ("".join(random.choice(letters) for i in range(password_length)))
                                
                                print("\u001b[35;1mYour generated password is: \u001b[0m",auto_gen_password)
                                new_user_password = auto_gen_password
                                print("input your generate password to proceed")
                            else:
                                print("Input your password")
                            while True:
                                userpassword = input()
                                if len(userpassword) >=6:
                                    save_user(create_user(username,userpassword)) # create and save new contact.
                                    print ('\n')
                                    print(f"Signed in as {username} ")
                                    print ('\n')
                                    break
                                else:
                                    print("Password too short!")
                                    continue

                            print("Use these short codes : nc - create a new credential, fi - Find a Credential , dc -delete a credential, sa- See all credential, ex -exit the app ")

                            if short_code == 'nc':
                                if short_code == 'nc':
                                    print("Create New Credential")
                                    print("-"*10)

                                    print ("Credential name ....")
                                    username = input()

                                    print("Password ...")
                                    print(" "*4 + "*the password must be 6 characters or longer*")
                                    print("Do you want your password Generated? Y/N")
                                    generate_pass =input().upper()
                                    if generate_pass == "Y":
                                        password_length = int(input("What length would you like your password to be,i.e 6,8..."))
                                        letters = string.ascii_lowercase
                                        auto_gen_password = ("".join(random.choice(letters) for i in range(password_length)))
                                
                                        print("\u001b[35;1mYour generated password is: \u001b[0m",auto_gen_password)
                                        new_user_password = auto_gen_password
                                        print("input your generate password to proceed")
                                    else:
                                        print("Input your password")


                                        while True:
                                            userpassword = input()
                                            if len(userpassword) >=6:

                                                save_user(create_user(username,userpassword)) # create and save new contact.
                                                print ('\n')
                                                print(f"New Account {username} {userpassword} created proceed to Sign in")
                                                print ('\n')
                                            break
                                        else:
                                            print("Password too short!")
                                    continue

                                
                                 
                            elif short_code == 'fi':
                                         print("Find the credential your Application")
                                         print("Input your Application")
                                         search_input= input()
                                         if check_existing_credential(search_input):
                                             print(f"\You have an account with us")
                                             break
                                         else:
                                             print("The credentials doesn't exist")
                                             continue

                            elif short_code == "dc":

                                            print("Application name:")
                                            app_name= input()
                                         

                                            if check_existing_credential(app_name):
                                             while True:
                                                 print("THIS WILL DELETE THE CREDENTIALS")
                                                 delete_credential = input()
                                                 delete_credential(delete_credential(app_name))
                                                 print("The credentials have been deleted")
                                                 continue

                            elif short_code == "sa":
                                         if len(Credential.credential_list) >=1:
                                             display_credential
                                             print("\nHERE ARE ALL YOUR CREDENTIALS")
                                             
                                             for credential in display_credential():
                                                 print(f'\Application Name: {credential.app_name} \n Username: {credential.credential_user_name} \n Password: {credential.credential_password}')
                                                 continue
                                             else:
                                                 print ("You don't have any credentials")
                                                 continue
                            elif short_code == "ex":
                                         print("\nYou have successfully logged out..\n")
                                         break
                            else:
                                         print("You did not select a valid option")
                                         
                elif short_code =="du":
                    print("Input User Name:")
                    user_name= input()
                    if check_existing_user(user_name):
                        while True:
                             print("THIS WILL DELETE THE CREDENTIALS")
                             delete_user = input()
                             delete_user(delete_user(user_name))
                             print("The user has been deleted")
                             continue
        

                elif short_code == "ex":
                            print("Bye .......")
                            
                else:
                            print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':

    main()