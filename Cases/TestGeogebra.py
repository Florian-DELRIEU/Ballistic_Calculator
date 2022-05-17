import matplotlib.pyplot as plt
from Class import g, Ballistic_Object
from Solver import Solve
from numpy import cos,sin,arange

Y0 = 0
V0 = 10
alpha0 = 45

tf = 10
dt = 0.01

V0x = V0*cos(alpha0)
V0y = V0*sin(alpha0)

#x1 = arange(0,10,0.1)
#y1 = lambda x: -1/2*g * x**2/V0x**2 + V0y/V0x*x + Y0

A = Ballistic_Object(1,0,Y0,V0x,V0y,drag=0)
Solve(A,dt,tf)

t = arange(0,tf,dt)
x = lambda t: V0x*t
y = lambda t: -1/2*g*t**2 + V0y*t + Y0


plt.figure("XY plot")
plt.plot(x(t),y(t),"k--",label="Analytique")
#plt.plot(x1,y1(x1),"g--",label="y(x)")
plt.plot(A.list_x,A.list_y,"b-",label="Simulation")

plt.legend(loc="best")