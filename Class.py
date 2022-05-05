g = 9.81
P0 = 1.225 # pressure at sea level (bar)


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
