import os
p=input("Enter the path:")
fil=os.listdir(p)
#print(fil)
for i in fil:
    if i.endswith('.py'):
        print("Executable find..")