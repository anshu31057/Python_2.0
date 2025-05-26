
real_pass = (12334)

for i in range(1,4):
    print("Attempt",i)
    password = int(input("Password: "))
    if password == real_pass:
        print("Access Granted")
        break
    else:
        print("Incorrect password")
else:
    print("Access denied!! To much attempts ")