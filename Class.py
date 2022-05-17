import numpy
from numpy import sqrt,arctan,cos,sin

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
#        self.angle = arctan(self.vx/self.vy)

        self.V = sqrt(self.vx**2 + self.vy**2)
        self.A = sqrt(self.ax**2 + self.ay**2)

        self.color = "r"
        self.Name = ""

        self.list_t = []
        self.list_angle = []
        self.list_x = []
        self.list_y = []
        self.list_vx = []
        self.list_vy = []
        self.list_ax = []
        self.list_ay = []

    def set_velocity(self,V,alpha):
        alpha = numpy.deg2rad(alpha)
        self.vx = V*cos(alpha)
        self.vy = V*sin(alpha)

    def save_kinetics(self,t):
        self.list_t.append(t)
#        self.angle = arctan(self.vx/self.vy)
        self.list_x.append(self.x)
        self.list_y.append(self.y)
        self.list_vx.append(self.vx)
        self.list_vy.append(self.vy)
        self.list_ax.append(self.ax)
        self.list_ay.append(self.ay)
