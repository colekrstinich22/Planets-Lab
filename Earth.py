from Planet import *

class Earth(Planet):

    def __init__(self,radius, color, centerX, centerY, window):
        super(Earth, self).__init__(radius,color,centerX,centerY,window)

    def buildContinent(self,window):
        continent = Polygon(Point(self.centerX+self.radius /10.9,self.centerY + self.radius / 1.7),Point(self.centerX-self.radius/1.7,self.centerY-self.radius/ 1.5),Point(self.centerX+self.radius/2,self.centerY-self.radius/1.2),Point(self.centerX+self.radius/7.1,self.centerY-self.radius/4.5),Point(self.centerX-self.centerY/28,self.centerY-self.centerX/9))
        continent.setFill("forest green")
        continent.draw(window)
        continent2 = Circle(Point(225, 310), 10)
        continent2.draw(window)
        continent2.setFill("forest green")

        #continent = Polygon(Point(self.centerX +20,300),Point(self.centerX+10,300),Point(self.centerX,350))


