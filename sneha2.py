print("TASK APP")
Main_Task = []
task1 = input("ENTER YOUR TASK ")
Main_Task.append(task1)
task2 = input("ENTER YOUR TASK")
Main_Task.append(task2)
task3 = input("ENTER YOUR TASK")
Main_Task.append(task3)
print(''' Enter your choice
      1. ADD TASK
      2. DELETE TASK''')
anshi = int(input(":"))
task4 = ""
if anshi == 1:
    task4 = input("ENTER YOUR TASK")
    Main_Task.append(task4)
elif anshi == 2:
    print("which Main_Task do you want to delete?")
    print("1",task1)
    print("2",task2)
    print("3",task3)
    if task4 != 0:
        print("4",task4)
    beniwal = int(input(":"))
    if beniwal == 1:
        Main_Task.remove(task1)
    elif beniwal == 2:
        Main_Task.remove(task2)
    elif beniwal == 3:
        Main_Task.remove(task3)
    elif beniwal == 4:
        Main_Task.remove(task4)
    else:
        print("INVALID SELECTION")
print("FINAL LIST:----")
if len(Main_Task) == 1:
    print("1.", Main_Task[0])
elif len(Main_Task) == 2:
    print("1.", Main_Task[0])
    print("2.", Main_Task[1])
elif len(Main_Task) == 3:
    print("1.", Main_Task[0])
    print("2.", Main_Task[1])
    print("3.", Main_Task[2])
elif len(Main_Task) == 4:
    print("1.", Main_Task[0])
    print("2.", Main_Task[1])
    print("3.", Main_Task[2])
    print("4.", Main_Task[3])
print("Length of list is:- ",len(Main_Task))           