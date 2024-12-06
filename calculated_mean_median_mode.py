#def add (a,b):
    #return a+b

#print(add(5,4))
#def capitalize(f_name,s_name):
    #name_person=f_name.capitalize(),s_name.title()
    #return name_person

#print(capitalize("avinash","jenny"))


#def area_of_rectangle():
   # l=int(input("enter a lenght: "))
   # wid=int(input("enter a width: "))
   # area = wid*l
   # return f"area of rectangl:{area}"
#print(area_of_rectangle())
from collections import Counter
def mean_med_mode(list1):

    mean = sum(list1) / len(list1)

    sorted_value=sorted(list1)
    n=len(sorted_value)

    if n%2==0:
        med=(sorted_value[(n // 2)-1] +sorted_value[n // 2]) /2

    else:
        med=sorted_value[n // 2]
        
        
    data=Counter(list1)
    mode_da=data.most_common()
    max_count=mode_da[0][1]
    mode=[val for val,count in mode_da if count== max_count]
    return mean, med, mode

print(f"Mean: {mean_med_mode([1, 2, 2, 3, 4, 4, 4, 5])[0]}, Median: {mean_med_mode([1, 2, 2, 3, 4, 4, 4, 5])[1]}, Mode: {mean_med_mode([1, 2, 2, 3, 4, 4, 4, 5])[2]}")
