from Graphics import *
from Planet import *

class Saturn(Planet):
    def __init__(self,radius,color,centerX,centerY,window):
        super(Saturn,self).__init__(radius,color,centerX,centerY,window)

    def drawRings(self,window):
        width = 1
        while width<2:
            rings=Arc(Point(self.centerX-self.radius*2*width,self.centerY+self.radius/2),Point(self.centerX+self.radius*2*width,self.centerY-self.radius/2),116,307,"ARC")
            rings.setWidth(1)
            rings.setOutline("dark khaki")
            rings.draw(window)
            width +=.1