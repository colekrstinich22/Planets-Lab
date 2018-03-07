from graphics import *
class Planet(object):

    def __init__(self,radius,color,center:Point):
        self.radius = radius
        self.color = color
        self.center = center

    def buildPlanet(self,radius,color,center:Point):
        planet = 