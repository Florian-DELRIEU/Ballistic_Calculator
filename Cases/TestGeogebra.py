import matplotlib.pyplot as plt
from Class import g, Ballistic_Object
from Solver import Solve
from numpy import cos,sin,arange

Y0 = 0
V0 = 10
alpha0 = 45

V0x = V0*cos(alpha0)
V0y = V0*sin(alpha0)

x = arange(0,10,0.1)
y = lambda x: -1/2*g * x**2/V0x**2 + V0y/V0x*x + Y0

A = Ballistic_Object(1,0,Y0,V0x,V0y,drag=0)
Solve(A,0.01,10)

plt.figure("XY plot")
plt.plot(x,y(x),"k--",label="Analytique")
plt.plot(A.list_x,A.list_y,"b-",label="Simulation")

plt.legend(loc="best")