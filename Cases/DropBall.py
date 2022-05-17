from Class import *
from Solver import Solve
import matplotlib.pyplot as plt
from numpy import cos,tan,arange

Initial_velocity = 100
Initial_angle =  -45
Initial_altitude = 400

Ball = Ballistic_Object(m=1,y=Initial_altitude,drag=0)
Ball.set_velocity(Initial_altitude,Initial_angle)
Ball.color = "b"

Solve(Ball,dt=0.01,tf=2)
print(f"La ball percute le sol après {Ball.list_t[-1]} secondes")

##
plt.figure("Ballistic")
plt.plot(Ball.list_x,Ball.list_y,f"{Ball.color}-",label ='50 kg')
plt.plot(Ball.list_x[-1],Ball.list_y[-1],f"{Ball.color}o")
