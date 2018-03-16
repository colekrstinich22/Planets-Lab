from Saturn import *
from Earth import *
import random
class SolarSystem(object):
    def __init__(self,window):
        """still thinking through"""
        self.drawPlanets(window)
    def drawPlanets(self,window):
        for i in range(1000):
            star=Circle(Point(random.randint(1,999),random.randint(1,649)),1)
            star.setFill("white")
            star.draw(window)
        earth = Earth(65,"blue",200,300,window)
        earth.buildContinent(window)
        saturn = Saturn(100, "khaki", 670, 400, window)
        saturn.drawRings(window)
