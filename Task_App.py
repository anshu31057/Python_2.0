print("TASK APP")

print("Enter Your Task:-")
tsk1 = input(":")
print("Enter Your Task:-")
tsk2 = input(":")

lissst = [tsk1,tsk2]
print('''Enter correct Choice:-
        1. Enter a task.
        2. Delete a task ''')
usr_input = int(input(":"))
tsk3 = ""
if usr_input == 1:
    tsk3 = input("Enter Your Task:- ")
    lissst.append(tsk3)
    
elif usr_input == 2:
    print("Which Task do you want to delete?")
    print("1.",tsk1)
    print("2.",tsk2)
    if tsk3 != "":
        print("3.",tsk3)

    usr_input2 = int(input(":"))
    if usr_input2 == 1:
        lissst.remove(tsk1)
    elif usr_input2 == 2:
        lissst.remove(tsk2)
    elif usr_input2 == 3 and tsk3 in lissst:
        lissst.remove(tsk3)
    else:
        print("Invalid Option Selected!!!!!!!")
print("FINAL LIST:----")
if len(lissst) == 1:
    print("1.", lissst[0])
elif len(lissst) == 2:
    print("1.", lissst[0])
    print("2.", lissst[1])
elif len(lissst) == 3:
    print("1.", lissst[0])
    print("2.", lissst[1])
    print("3.", lissst[2])


print("Total number of task in your list:- ",len(lissst))