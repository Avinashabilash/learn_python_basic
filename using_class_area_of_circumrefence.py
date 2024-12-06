
## area_of_triangle:
class Triangle:
    def __init__ (self,b,h):
        self.base = b
        self.height = h
    def area_of(self):
            area=1/2 * self.base * self.height
            print(area)
            #return area


bandh = Triangle(20, 34)
area_of_triangle = bandh.area_of()

area_of_triangle
   
    

#class circle:
    #pi=3.14 # class attributes
    #def __init__(self,r):
    #    self.radius=r
    #def cricumrefence(self):
      #  print(self.pi*self.radius**2)
#radii=circle(90)
#area_of_circle=radii.cricumrefence()

#radii_1=circle(34)
#area_of_circle=radii_1.cricumrefence()
