## no_of_in year_even_finding_does_it_leap_year##
def number_day ():
    year=int(input("enter a year: "))
    month=int(input("enter a month: "))
    if (year%4==0 and year%400==0) or (year%100!=0):
        is_leap_year= True 
    else:
       is_leap_year =False

    days_list=[31,28,3,30,31,30,31,31,30,31,30,31]
    
    if is_leap_year and month == 2:
        return 29
    else:
         return days_list[month-1]
            
print(number_day())
  
