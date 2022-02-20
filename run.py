#!/usr/bin/env python3.9
from user import User
from credential import Credential
def create_user(userName,userPassword):
    """
    Function to create User
    """
    new_user = User(userName,userPassword),
    return new_user

def create_credential(appName,credentialName,credentialPassword):
    """
    Function to create Credential
    """
    new_credential = Credential(appName,credentialName,credentialPassword),
    return new_credential

def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()

def save_credential(credential):
    '''
    Function to save credential
    '''
    credential.save_credential()

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

def find_credential(credential):
    '''
    Function that finds the credentials from the app name
    '''
    return Credential.find_by_app(credential)

def check_existing_user(user):
    '''
    Function that check if a user exists and returns a Boolean
    '''
    return User.user_exist(user)

def check_existing_credential(credential):
    '''
    Function that check if a credential exists and returns a Boolean
    '''
    return Credential.credential_exists(credential)

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