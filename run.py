#!/usr/bin/env python3.6
from credentials import Credentials
import user
import random


def create_user(fname, lname, phone, email):
    '''
    Function to create a new user
    '''
    new_user = (fname, lname, phone, email)
    return new_user


def save_user(user):
    """
    Function to save user
    """
    user.save_user_details()


def create_credential(uname, pword, email):
    """
    Function to create new user credentials
    """
    new_credential = Credentials(uname, pword, email)
    return new_credential


def save_credential(credential):
    """
    Function to save user credentials
    """
    credential.save_credential()


def delete_credentials(credential):
    """
    Function to delete all users credentials
    """
    credential.delete_credential()


def display_credential(Credentials):
    '''
    Function that displays credentials
    '''
    return Credentials.display_credential()


def display_user(user):
    """
    Function that returns saved users
    """
    return user.display_users()


def main():
    print("Hello! Welcome to Password-Locker")
    print("Choose action you would wish to take")
    print('-'*100)
    while True:
        print("Kindly use this short codes \n CU: To create new user account\n LG: To log in to existing account \n DA: To display list of accounts \n EX:To exit")
        short_code = input()
        if short_code == 'cu':
            print("welcome. Follow this simple steps to Create an account")
            print('-'*50)
            print("What site would you like to generate an account for")
            site = input()
            print("First name ....")
            f_name = input()
            print('Last name....')
            l_name = input()
            print("Enter Phone Number")
            phone = input()
            print('Enter email address ....')
            email = input()
            print('\n')
            print("How would you love your password? \n pp:To generate own password \n pg:Have password generated for you")
            password = input()
            if password == 'pp':
                print("Enter Password....")
                password = input()
                print(f"Hello {f_name} your password has been generated")
                print('-'*50)
            else:
                print(
                    f" Hey {f_name}, a new password will be generated for you.")
                s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
                pword = "".join(random.sample(s, 8))
                print(f"Hey {f_name}, you new {site} password is {pword}")
                break

            print('\n')
            print(
                f"Please confirm your details fname:{f_name} lname:{l_name}  phone:{phone} email:{email}")
            print("Enter 'y' to continue or 'n' to input new data")
            response = input()
            if response == 'y':
                print(
                    f"Hello {f_name} {l_name} . Your account has been successfuly created.")
            else:
                 print(
                     "Kindly use this short codes \n CU: To create new user account\n LG: To log in to existing account \n DA: To display list of accounts \n EX:To exit")
            break
    save_user(create_user(f_name, l_name, phone, email))
       elif short_code == 'da':
            print("-"*50)
            print("Enter UserName...")
            UserName = input()
            print('-'*100)
            print("Am afraid the user is not registered with us...")
            break
        elif short_code == 'lg':
            print("Welcome.What site would you love to log into?")
            site = input()
            user_name = input("User name: ")
            password = input("password: ")
            print(f"Welcome {user_name} Your credentials have been received.")
            print(f"Welcome to {site}. Have fun!")
            break
           
        elif short_code == 'ex':
            print("Thank for Visiting Password-Locker.......See you soon!")   
            break  
            
            
        else:
            print("You have made an invalid choice. Please try again")
            print('-'*100)
            
if __name__ == '__main__':
    
    main()
    
