import csv
import os
import Customer as cst

file = open('CustomerLogin.csv','r')
file2 = open('Authentication.csv','r')
admin_authentication = list(csv.reader(file2,delimiter=","))
customer_credentials = list(csv.reader(file,delimiter=","))

def login():
    attempts = 0
    access_granted = False
    while (attempts < 3):
        id = input("Enter id: ")
        for j in customer_credentials:
            if (j[0] == id):
                password = input("Enter password: ")
                if (j[1] == password):
                    print("Access granted")
                    access_granted = True 
                    cst.customer_input()
                    break
                else:
                    print("Wrong password")
                    attempts += 1
                    break
        else:
            print("Wrong id")
            attempts += 1
    if not access_granted:
        print("You have reached the login limit")

def signup():
    customer_signup = open("customer.csv","a")
    new_id = input("Enter a new id: ")
    for j in customer_credentials:
        if (j[0] == new_id):
            print("Id already exists. Please try again.")
            break
    else:
        new_password = input("Enter a new password: ")
        confirm_password = input("Confirm password: ")
        if new_password == confirm_password:
            customer_signup.write("\n")
            customer_signup.write(new_id + "," + new_password)
            print("Sign up successful!")
            login()
        else:
            print("Passwords do not match. Please try again.")


def Admin_auth():
    attempts = 0
    access_granted = False
    while (attempts < 3):
        id = input("Enter id: ")
        for j in admin_authentication:
            if (j[0] == id):
                password = input("Enter password: ")
                if (j[1] == password):
                    print("Access granted")
                    attempts = 3
                    access_granted = True
                    break
                else:
                    print("Wrong password")
                    attempts += 1
                    break
        else:
            print("Wrong id")
            attempts += 1
    if not access_granted:
        print("You have reached the login limit")
