n=input("enter a name")
slipted=n.split(" ")
print(len(n))
for i in range(1,6):
    print(i,slipted[i-1])
    if i==4:
        print("welcome")
print("successfully completed")
