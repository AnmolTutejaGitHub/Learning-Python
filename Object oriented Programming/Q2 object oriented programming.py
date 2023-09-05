#object oriented programming
# #Fill in the class
# class Cylinder:
    
#     def __init__(self,height=1,radius=1):
#         pass
        
#     def volume(self):
#         pass
    
#     def surface_area(self):
#         pass

# # EXAMPLE OUTPUT
# c = Cylinder(2,3)
# c.volume()
# c.surface_area()

class Clyinder:
    def __init__(self,height=1,radius=1):
        self.height=height
        self.radius=radius

    def volume(self):
        return self.height*3.14*(self.radius)**2
    
    def surface_area(self):
        top=3.14*(self.radius**2)
        return (2*top)+(2*3.14*self.radius*self.height)
    
    
mycyl=Clyinder(2,3)
print(mycyl.volume())
print(mycyl.surface_area())

