#   FILE ME KUCH WRITE KRNA HO TOH 
# file = open("sample.txt","w")
# file.write("Hello, Guyss!!")
# file.close

# FILE READ KRNII HO TOH 
file = open("sample.txt","r")
content = file.read()
print(content)
file.close

#FILE ME KUCH LAST ME ADD KRNA HO TOH 
# f = open("sample.txt","a")
# f.write("\nNew Line Added")
# f.close()

# # Append se last me add hota h file k and write se vo over write ho jatii h phla sara data del ho jata h 
# with open("sample.txt","r") as f:
#     print(f.read())