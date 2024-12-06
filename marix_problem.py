x=input("enter a row and column for 3*3 number: ")
list_1=[1,0,1]
list_2=[1,1,1]
list_3=[1,2,1]
final_list=[list_1,list_2,list_3]
#print(final_list)
print(len(final_list))
print(f" {list_1}\n {list_2}\n {list_3}\n")
#final_list[0][1]=("X")
#print(final_list)

if x == "00":
    final_list[0][0] = "X"
    print(final_list)
elif x == "01":
    final_list[0][1] ="X"
    print(final_list)
elif x == "02":
    final_list[0][2] ="X"
    print(final_list)
elif x == "10":
    final_list[1][0] ="X"
    print(final_list)
elif x == "11":
    final_list[1][1] = "X"
    print(final_list)
elif x == "12":
    final_list[1][2] ="X"
    print(final_list)
elif x == "20":
    final_list[2][0] ="X"
    print(final_list)
elif x == "21":
    final_list[2][1] ="X"
    print(final_list)
elif x == "22":
    final_list[2][2] = "X"
    print(final_list)
else:
    print("inalid syntax")

                   
