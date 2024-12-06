#a=10
def display():
    a=20
    def show():
        global a
        a=30
    print(a)
    show()
    print (a)
display()

name ="jenny"
def display():
    global name
    name=name+" ram"
print(name)
display()
print(name)
