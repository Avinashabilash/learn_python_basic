## use getter and setter 
class solution:
    def __init__(self,public,protected,private):
        self.public=public
        self._protected=protected
        self.__private=private
    def get_private(self):
        return self.__private

    def set_private(self,private):
         self.__private=private
         if self.__private == "praveen":
             print("hi")
       

    def display_private_data(self):
        return self.__private
        
d=solution("praveen","abilash","avinash")
print(d._solution__private)
print(d.display_private_data())
print(d.get_private())
d.set_private("praveen")
print(d.get_private())

