print("TASK APP")
task = []
tsk1 = input("Enter your task:-")
task.append(tsk1)
tsk2 = input("Enter your task:-")
task.append(tsk2)
tsk3 = input("Enter your task:-")
task.append(tsk3)
print('''Enter Your Choice:-
            1. Add new task
            2. Delete a task''')
a = int(input(":"))
tsk4 = ""
if a == 1:
    tsk4 = input("Enter your task:-")
    task.append(tsk4)
elif a == 2:
    print("Which task do you want to delete?")
    print("1.",tsk1)
    print("2.",tsk2)
    print("3.",tsk3)
    if tsk4 != "":
        print("4.",tsk4)
    
    usr_input = int(input(":"))
    if usr_input ==1:
        task.remove(tsk1)
    elif usr_input == 2:
        task.remove(tsk2)
    elif usr_input == 3:
        task.remove(tsk3)
    elif usr_input == 2:
        task.remove(tsk4)
    else:
        print("INVALID OTION")
else:
    print("INVALID SELECTION")
print("FINAL LIST:----")
if len(task) == 1:
    print("1.", task[0])
elif len(task) == 2:
    print("1.", task[0])
    print("2.", task[1])
elif len(task) == 3:
    print("1.", task[0])
    print("2.", task[1])
    print("3.", task[2])
elif len(task) == 4:
    print("1.", task[0])
    print("2.", task[1])
    print("3.", task[2])
    print("4.", task[3])

print("Length of list is:- ",len(task))






