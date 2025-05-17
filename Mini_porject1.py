import os

folder_path = input("Enter folder path: ")
files = os.listdir(folder_path)  # listdir se folder me jo bhi h list ho jata h 
print("Files in folder\n",folder_path,":")
for item in files:
    print("-",item)   # is for item in files ka mtlb h jitne items h folder me tab tak is print ko run krte rho 
