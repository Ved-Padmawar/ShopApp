import csv
import pandas as pd
import datetime


def customer_input():
        List = []
        df = pd.read_csv("Products.csv") 
        print(df)
        for i in range(int(input("Enter number of products to buy: "))):
            items = input().split()
            List.append([(items[0].upper()),int(items[1])])
        
        shop(List)

def shop(cart): 
    final_cart = []
    final_data = []
    Total_amount = 0
    file = open("Products.csv","r")
    data = list(csv.reader(file,delimiter=","))
    for i in data:
        final_data.append([i[0], i[1], int(i[2]), int(i[3])])
    print("Your Products: ")
    print(cart)
    for i in cart:
        for j in final_data:
            if (i[0] == j[0]):
                if (i[1] <= j[3]):
                    bill = i[1] * j[2]
                    Total_amount = Total_amount + bill
                    final_cart.append(i)
                elif (i[1] <= j[3] and j[3] != 0):
                    print("The quantity asked by u for",i[0],"is not available only",j[3],"is available do u want",j[3])
                    ch = input("Y/N: ").upper()
                    if (ch == 'Y'):
                        del(cart[1])
                        i[1] = j[3]
                        bill = j[2] * i[1]
                        Total_amount = Total_amount + bill
                        final_cart.append(i)
                    else:
                        print("Not enough stock available",i[0])
                        continue
                else:
                    print("Not enough stock available",i[0])
    print("1.Checkout\n2.Continue Shopping")
    continue_shopping = int(input("Enter your choice: "))
    if (continue_shopping == 1):
        reciept(final_data,final_cart,Total_amount)
    else:
        customer_input()
    print("Final Cart: ")
    print(final_cart)
    print(len(final_cart))
    print("Total amount to pay: ",Total_amount)

def reciept(final_data,final_cart,Total_amount):
    order_number = generate_order_number()
    print("Receipt: ")
    print("Product Name\t\tQuantity\tPrice\tAmount")
    print("cart length: ", len(final_cart))
    for i in final_cart:
        for j in final_data:
            if (i[0] == j[0]):
                print(j[1],"\t\t",i[1],"\t\t",j[2],"\t",i[1]*j[2])
                break
    print("\nTotal amount to pay:", Total_amount)
    print("Order number: ", order_number)
    exit()

def generate_order_number():
    order_number = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    return order_number
