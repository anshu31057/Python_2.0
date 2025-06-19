def add(**contacts):
    print("Enter Name:- ")
    name = input(": ")
    phone = int(input("Enter Number:- "))
    contacts[name] = phone
contacts = {}
while True:
    print("PHONE DAIRY")
    print("-----------")
    print(
        """1. Add
2. Search
3. Delete
4. View all
5. Exit"""
    )
    print("-----------")
    a1 = input(": ")
    if a1 == "1":
        add(contacts=contacts)
