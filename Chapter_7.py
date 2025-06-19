#Functions!!!
# def greet(name):
#     print("Hello",name)

# greet("Anshu")

# def add(a,b):
#     return a+b

# result = add(4,6)
# print(result)

# def gret(name="Guest"):
#     print("Hello,",name)
# gret()
# gret("Anshu")

# def square(x):
#     return x*x
# sqr = square(5)
# print(sqr)
import os
def guest_name(*guests , **details):
    os.system("cls")
    print("Inviting Guests: ")
    for guest in guests:
        print("-",guest)

    print("Event Detial:- ")
    for key in details:
        print(key,":",details[key])

guest_input = input("Enter Guests name(seprate with comma , ): ")
guest_list = guest_input.split(",")

venue = input("Enter Venue: ")
host = input("Enter host name: ")
time = input("Enter Time: ")

guest_name(*guest_list,venue=venue,host=host,time=time)
