from Graphics import *
class Planet(object):

    def __init__(self,radius,color,centerX,centerY,window):
        self.radius = radius
        self.color = color
        self.centerX = centerX
        self.centerY=centerY
        self.buildPlanet(window)

    def buildPlanet(self,win):
        planet=Circle(Point(self.centerX,self.centerY),self.radius)
        planet.setFill(self.color)
        planet.draw(win)


win=GraphWin("planet", 1000,650)
sun=Planet(100,"yellow",500,325,win)
win.getMouse()
win.close()