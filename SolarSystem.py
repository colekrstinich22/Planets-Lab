from Saturn import *

class SolarSystem(object):
    def __init__(self,window):
        """still thinking through"""
        self.drawPlanets(window)
    def drawPlanets(self,window):
        saturn = Saturn(100, "khaki", 670, 400, window)
        saturn.drawRings(window)