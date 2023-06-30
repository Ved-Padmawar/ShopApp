import pandas as pd  
import LoginSystem as ls
import Customer as cst
import Admin as A
import csv
count = 0
List = []
print("1.Customer")
print("2.Admin")
ch = int(input("Enter choice: "))
if (ch == 1):
    choice = int(input("Enter '1' to login or '2' to sign up: "))
    if (choice == 1):
        ls.login()
    if (choice == 2):
        ls.signup()
if (ch == 2):
    ls.Admin_auth()