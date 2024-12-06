def calculator():
    while True:
        fri_no=int(input("enter a number"))
        while True:
            print(f"\nm{"+","-","*","/"}")
            pick=input("pick an operation: ")
            se_no=int(input(" enter next number: "))

            if pick=="+":
                 c=fri_no+se_no
            elif pick == "-":
                c=fri_no-se_no
            elif pick == "*":
                c= fri_no*se_no
            elif pick == "/":
                if se_no!=0:
                    c=fri_no/se_no
                else:
                    print("error:in division by zero is not alloed")
            else:
                print("invalid operation . please choose a valid operation.")
            print(f" result:{c}")
   
            choise=input("enter 'y' to continue calculation with {c} or'n' to start to 'e' exit:")
            if choise=='y':
                fri_no = c
            elif choise=="n":
                break
            elif choise == "e":
                return
            else:
                print( "invalid choice")

print(calculator())
