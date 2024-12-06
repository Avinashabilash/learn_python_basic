### maximum_number find

n=input("enter a value: ")
maxi=n.split()
print(maxi)
lenght=len(maxi)
for i in range(lenght):
    maxi[i]=int(maxi[i])
print(maxi)




max_num=maxi[0]
for number in maxi:
    if number> max_num:
        max_num=number
print(max_num)
    
    
