
def Add():
    global contacts
    print("---------------------------")
    print("Enter Your Choice Down")
    print("---------------------------")
    
    print("\nEnter 1234 to go back to main menu")
    while True:
        phone = input("Enter Contact number: ")
        if phone == "1234":
            break
        name = input("Enter Name: ").lower()
        if name == "1234":
            break
    contacts[name] = phone
    print("Contact Saved Successfully!!")


while True:
    print("PHONE DIARY")
    print(
        """1. Add
2. Search
3. Delete
4. View all
5. Exit"""
    )
    opt = int(input(":"))
    if opt == 1:
        Add()

    elif opt == 2:
        while True:
            print("Search By Name or Phone no.")
            print(
                """1. Name
2. Phone no.
Enter 1234 to exit"""
            )
            a1 = int(input(": "))
            if a1 == 1:
                b1 = input("Enter Name: ").lower()
                if b1 in contacts:
                    print(":", contacts.get(b1))
                else:
                    print("Contact Not Found!!")
            elif a1 == 2:
                b2 = input("Enter Number: ")
                for key, values in contacts.items():
                    if values == b2:
                        print(":", key)
            elif a1 ==1234:
                break
    elif opt == 3:
        a2 = input("Enter Name to delete:").lower()
        contacts.pop(a2, None)
        print("Deleted Successfullly!!")
    elif opt == 4:
        for phone, name in contacts.items():
            print("---------------------------")
            print(phone, ":", name)
    elif opt == 5:
        break
