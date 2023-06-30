import csv 
def Admin_portal():
    final_data = []
    stock = []
    file = open("Products.csv","r")
    file2 = open("Products.csv","a")
    data = list(csv.reader(file,delimiter = ","))
    for i in data:
        final_data.append([i[0], i[1], int(i[2]), int(i[3])])
    print("1.Add stock\n2.New Product")
    choice = int(input("Enter your choice: "))
    if (choice == 1):
        add_stock = input().split()
        stock.append([add_stock[0].upper(),int(add_stock[1])])
        for i in final_data:
            for j in stock:
                if (i[0] == j[0]):
                    i[3] = i[3] + j[1]
        print(final_data)
    if (choice == 2):
        quantity = int(input("Enter number of products to add: "))
        for i in range (0, quantity):
            id = input("Enter product id: ").upper()
            product_name = input("Enter prooduct name: ")
            product_quantity = input("Enter total stock: ")
            product_price = input("Enter product price: ")
            file2.write("\n")
            file2.write(id + "," + product_name + "," + product_quantity + "," + product_price )