from Graphics import *
from Planet import *

class Saturn(Planet):
    def __init__(self,radius,color,centerX,centerY,window):
        super(Saturn,self).__init__(radius,color,centerX,centerY,window)

    def drawRings(self,window):
        rings=Arc(Point(self.centerX-self.radius*2, self.centerY+self.radius/2),Point(self.centerX+self.radius*2, self.centerY- self.radius/2), 117,306,"ARC")
        rings.setWidth(9)
        rings.setOutline("dark khaki")
        rings.draw(window)
