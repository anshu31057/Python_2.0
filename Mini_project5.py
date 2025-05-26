pedia = {'boy':'Ladka', 'girl': 'Ladki', 'money':'Paisa'}
word = input("Enter Your Word you have to translate:-")
word = word.lower().strip()
if word in pedia:
    print("The meanig of the",word, "is:-",pedia[word])
else:
    print("Sorry Not available in dictionary!!!")
