##program to calculate average height frpom a list of height
hits=input("enter a value: ")
h_list=hits.split()
lenght=0
for hits in h_list:
    lenght=(len(h_list))
print(lenght)
for i in range(lenght):
    h_list[i]=int(h_list[i])
    
print(h_list)



sum=0
for per in h_list:
    sum+=int(per)
avg=sum/lenght
print (round(avg))
    
