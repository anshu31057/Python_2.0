items = []
items = input("Enter your list of products(sepreated by comma):-").split(',')
items = [i.strip().lower() for i in items]
list_count = len(items)
list_unique = sorted(set(items))

print("Your List:-")
print("Your list items:- ", items)
print("Total number of items in list: ",list_count)

