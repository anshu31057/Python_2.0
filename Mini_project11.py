import os
class Student:
    def __init__(self,name,grade,maths, science,english):
        self.name = name
        self.grade = grade
        self.maths=maths
        self.science = science
        self.english = english
    def calculate_percnt_total(self):
        total = self.maths+self.science+self.english
        percent = total/3
        return total,percent
    def print_report(self):
        os.system("cls")
        total,percnet = self.calculate_percnt_total()
        print("Report Card For",self.name)
        print("Class: ",self.grade)
        # print("Marks: Maths =",self.maths,"Science = ",self.science," English = ",self.english)
        print(f"Marks: Maths = {self.maths}, Science = {self.science}, Englihs = {self.english}")
        print(f"Total out of 300:{total}")
        print(f"Percentage:{percnet}")
    def save_file(self):
        total,percent = copy.calculate_percnt_total()
        with open("Student_Data.txt", "a") as data:
            data.write("\n------------------------------\n")
            data.write(f"Student Name: {Name}\n")
            data.write(f"Class       : {Grade}\n")
            data.write(f"Maths       : {Maths}\n")
            data.write(f"Science     : {Science}\n")
            data.write(f"English     : {English}\n")
            data.write(f"Total       : {total}\n")
            data.write(f"Percentage  : {percent}\n")
            data.write("------------------------------\n")


#Taking inputs from user 
Name = input("Enter Name of Student:")
Grade = input("Enter Class: ")
Maths = int(input("Enter Maths Marks:"))
Science = int(input("Enter Science Marks:"))
English = int(input("Enter English Marks:"))
copy = Student(name=Name,grade=Grade,maths=Maths,science=Science,english=English)
copy.print_report()

#Saving Info in Computer

