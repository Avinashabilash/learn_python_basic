class solution(object):
    def getLastDigit(self,a,b):
        self.a=a
        self.b=b
    def power(self):
        c=self.a**self.b
        D=c%10
        print(f"last digit: {D}")

get_1=solution()
get_1.getLastDigit(3,4)
last_no=get_1.power()
last_no
