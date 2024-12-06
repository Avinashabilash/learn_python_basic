#dunder_learning_how to use
class naming:
    def __init__(self,name,book,page):
        self.name=name
        self.book=book
        self.page=page
    def __str__(self):
        return f"{self.book} by {self.name}"
    def __len__(self):
        return self.page
    def __call__(self,*args,**kwargs):
        print("Hi")
    
n=naming("avinash","life of sex",700)
print(n)
print(len(n))
n()
