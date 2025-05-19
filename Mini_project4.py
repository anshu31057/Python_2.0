string = input("Enter your Unclear, Unformated string:- ")
string = string.lower()
cleaned = " ".join(string.split())
print("Cleaned String:- ",cleaned)
