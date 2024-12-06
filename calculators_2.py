def calculation ():
    while True:
        def add (a,b):
            return a+b
        def sub (a,b):
            return a-b
        def mult (a,b):
            return a*b
        def divi (a,b):
            return a/b
        operators={
            "+":add,
            "-":sub,
            "*":mult,
            "/":divi
            }
        fr_no=int(input("enter a frist number"))
        for symbol in operators:
            print(symbol)
        flag=True
        while flag:
            choice=input("pick any the symbol")
            se_no=int(input("enter a second number"))
            calculator_fun=operators[choice]
            output=calculator_fun(fr_no,se_no)
            print(f"{fr_no} {choice} {se_no}={output}")

            next_1=input("enter 'y' to continue calculation with {output} or 'n' to start 'e' to exit").lower()
            if next_1=='y':
                fr_no=output
            elif next_1 == 'n':
                break
            elif next_1 =='e':
                return
            else:
                print ("i navild choice")

print( calculation())
