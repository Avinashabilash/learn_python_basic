class Father:
    def sleep(self):
        print("sleeps from 10:00 pm to 5:00am")
    def eat(self):
        print("eating")
class son(Father):
    def sleep(self):
        print("sleeps from 2:00 am to 12:00am")
        super().sleep()

avi=son()
avi.sleep()
