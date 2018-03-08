from Planet import *

class Earth(Planet):

    def __init__(self,radius,color,centerX,centerY,continent,window):
        super(Earth, self).__init__(radius,color,centerX,centerY,window)
        self.continent = continent
        self.buildEarth(window)

    def buildEarth(self,win):
        pass


win = GraphWin("Test", 1000, 650)
earth = Earth(100, "blue", 400, 200, "uhhhhhhh", win)

win.getMouse()
win.close()


