"""This script consists of a class Sphere functions required to calculate the circumference, surface area, and volume of astronomical objects such as the Earth, Moon and Sun."""


class Sphere:                                     # define the spherical class
    import math as ma 
    global ma                                     # define the imported math module globally
    
    def __init__(self, name, radius):
        self.name = name                           # renders the name in an instance variable self.radius
        self.radius = radius                       # renders the radius in an istance variable self. radius
         
    def getRadius(self):
        print("The radius of the {} is {} km." .format(self.name,self.radius))
    
    def getCircumference(self):  # method to calculate the circumference                  
        self.circum = 2*ma.pi*self.radius           
        return self.circum
    
    def surfaceArea(self):      # method to calculate the surface area
        self.area = ma.pi*(self.radius)**2           
        return self.area
  
    def volume(self):            # method to calculat  volume
        self.volum = (4/3)*ma.pi*(self.radius)**3    
        return self.volum
    
    def printResults(self):      # methods to print out the result
        print("The {} has the following parameters:\nRadius = {} km\n\
Circumference = {} km\nSurface Area = {:.2e} km\u00b2\nVolume = {:.2e} km\u00b3\
        " .format(self.name,round(self.radius,1),round(self.circum,1),self.area,self.volum))  # print results in an expenoential form
        
def main():    # defining the main function to generates the instances of the sphere class
    Earth = Sphere("Earth",6371)   # for the Earth instance
    Earth.getRadius()
    Earth.getCircumference()
    Earth.surfaceArea()
    Earth.volume()
    Earth.printResults()
    print("  ")
    
    Moon = Sphere("Moon",1737)   # for the Moon instance
    Moon.getRadius()
    Moon.getCircumference()
    Moon.surfaceArea()
    Moon.volume()
    Moon.printResults()
    print("  ")
    
    Sun = Sphere("Sun",695700)   # for the Sun instance
    Sun.getRadius()
    Sun.getCircumference()
    Sun.surfaceArea()
    Sun.volume()
    Sun.printResults()
    
if __name__ == "__main__":main() # This enables the main() function to be executed if the module is executed without importing