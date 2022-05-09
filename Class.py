from numpy import sqrt

g = 9.81
Rho = 1.225 # air density at sea level (bar)


class Ballistic_Object:
    def __init__(self,m=5,x=0,y=0,vx=0,vy=0,surface=1,drag=0.1):
        self.mass = m
        self.surface = surface
        self.drag_coefficient = drag
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.ax = 0
        self.ay = 0

        self.V = sqrt(self.vx**2 + self.vy**2)
        self.A = sqrt(self.ax**2 + self.ay**2)

        self.color = "r"
        self.Name = ""