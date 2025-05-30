def event(*people,**details):
    print("Invited Peoples Name:- ")
    for guest in people:
        print("-",guest)
    
    print("Event Details:-")
    for key in details:
        print(key,":",details[key])

people = input("Enter Name of Peoples(Seprated With Coma: ): ").upper().split(",")

venue = input("Enter Venue:- ")
host = input("Enter Host Name:- ")
time = input("Enter Time:- ")
event(*people,venue=venue,host=host,time=time)