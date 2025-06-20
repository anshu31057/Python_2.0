# OOPS 
# Making class 
class Students:
    def __init__(self,name,age):
        self.name = name
        self.age = age

s1 = Students("Anshu",18)
print(s1.name)
print(s1.age)

# Another Exapmle

class Greet:
    def __init__(self,name):
        self.name = name

    def greet(self):
        print("Hello",self.name)
s1 = Greet("Anshu")
s1.greet()
        