"""This script consists a class point that use the provided initial x and y cordinates,length and the angle of rotation in degrees then calculates the remaining points and plots them to form a class square.The script was written through visting different references including https://en.wikipedia.org/wiki/Trigonometric_functions """
class Point:
    
    def __init__(self, x=0.0, y=0.0): # the initial value for x and y coordinates set to 0 
        self.x = x
        self.y = y

class Square:
    
    def __init__(self, points, length, rotation): 
        self.points = points       # the x and y cordinates for the first point definng x axis before y axis
        self.length = length       # Length of the square
        self.rotation = rotation   # Rotation angle of the square
    
    def getCorners(self):
        import math as ma # imported math module as ma
        import matplotlib.pyplot as plt # imports matplotlib.pylot as plt
        p1x = self.points[0]            # define the x-axis of first point
        p1y = self.points[1]            # define the y-axis of first point
        # calculations the other remaining points using trigonometry functions
        p2x = p1x+(self.length*ma.cos(ma.radians(self.rotation)))
        p2y = p1y+(self.length*ma.sin(ma.radians(self.rotation)))
        p4x = p1x+(self.length*ma.sin(ma.radians(self.rotation)))
        p4y = p1y-(self.length*ma.cos(ma.radians(self.rotation)))
        p3x = p4x+(self.length*ma.cos(ma.radians(self.rotation)))
        p3y = p4y+(self.length*ma.sin(ma.radians(self.rotation)))
        sq_corners = ([p1x,p2x,p3x,p4x,p1x],[p1y,p2y,p3y,p4y,p1y])
        
        self.sqcorners = sq_corners                       # variable accepts the square corners
        line =([p1x,max(self.sqcorners[0])+2],[p1y,p1y])  # the function draw a line on the plot
        
        print("The square formed with rotation angle {}" .format(self.rotation)) # print the square geometry 
        print("The four corners points of the square are:")   # print out the four corners of a square
        print("x, y")  
        for i in range(0,len(self.sqcorners[0])):
            print("{}, {}".format(round(self.sqcorners[0][i],2),round(self.sqcorners[1][i],2)))
        
        #The remaining codes plots the square with labels
        plt.plot(self.sqcorners[0],self.sqcorners[1],"bo-")
        plt.plot(self.sqcorners[0][0],self.sqcorners[1][0],"ko")
        plt.plot(line[0],line[1],"g-")
        plt.xlabel('x (m)')
        plt.ylabel('y (m)')
        plt.title("Square")
        plt.axis([min(self.sqcorners[0])-0.2, max(self.sqcorners[0])+0.2, min(self.sqcorners[1])-0.2, max(self.sqcorners[1])+0.2])
        plt.text(self.sqcorners[0][0]+0.5,self.sqcorners[1][0]+0.1 , str(self.rotation)+'\N{DEGREE SIGN}')
        plt.rcParams['figure.figsize'] =[self.length+1,self.length+1]
        plt.show()