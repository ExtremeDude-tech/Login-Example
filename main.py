import requests
import os
import time
import sys
import getpass
import os.path
import re 

from colorama import Fore, init
from re import search


logo = """
Logo example"""

if not os.path.exists("login.extremedev"):
    login()


def login():
    os.system("cls")
    os.system("title Login Example ")
    print()
    print(logo)
    print()
    print("Login Example by ExtremeDev")
    print()
    name = input("What's your username:")
    print()
    print("Loading username: {}".format(name))
    time.sleep(1)
    print()
    os.system("cls")
    print()
    print(logo)
    print()
    print("Login Example by ExtremeDev")
    print()
    password = input("Enter your password:")
    print("Loading password: {}".format(password))
    time.sleep(1)
    with open("login.extremedev", "a+") as e:
        e.write(f"\"Login\": \"{name}:{password}\"")
    print("Please reopen application\nYour login is correct..")
    time.sleep(2)
    input("Press any key to quit.")
    sys.exit()
def main():
    os.system("cls")
    os.system("title Login Example by ExtremeDev")
    with open("login.extremedev", "r+") as read:
        extreme = read.readlines()
        login = re.search(r'\"Login\": \"(.*?):(.*?)\"', str(extreme)).groups(2)
    print()
    print(logo)
    print()
    print("You logged succesfully")
    print()
    print("  Detail of login")
    print("===================")
    print("Username: {}".format(login[0]))
    print("Password: {}".format(login[1]))
    print("===================")
    print()
    print("Change Username: [1]")
    print("Change Password: [2]")
    alegere_menu = input("")
    if alegere_menu == "2":
        print("Enter your new password:")
        new_pass = input("")
        with open("login.extremedev", "w+") as e:
            e.write(f"\"Login\": \"{login[0]}:{new_pass}\"")
            print("Password changed succesfully..")
            time.sleep(2)
            input("Press any key to quit..")
    elif alegere_menu == "1":
        print("Enter your new username:")
        new_user = input("")
        with open("login.extremedev", "w+") as e:
            e.write(f"\"Login\": \"{new_user}:{login[1]}\"")
            print("Username changed succesfully")
            time.sleep(2)
            input("Press any key to quit..")
    else:
        print("Invalid input")
        time.sleep(2)
        main()
    
main()
