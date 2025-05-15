
#Taking Inputs
a = int(input("Enter Number 1: "))
b = int(input("Enter Number 2: "))

print('''Enter Your Choice:
      1. Addtion
      2. Subtract 
      3. Multipy
      4. Devide''')
c = int(input("---> "))

# Main Logic
if c == 1:
    print(a+b)
elif c ==2:
    print(a-b)
elif c == 3:
    print(a*b)
elif c == 4 :
    if b == 0:
        print("Not defined")
    else:
        print(a/b)
else:
    print("Chose Correct Option")

