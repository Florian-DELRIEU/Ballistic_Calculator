from Class import *
from Solver import Solve
import matplotlib.pyplot as plt

A = Ballistic_Object(m=1,vx=0,vy=10,drag=0)
B = Ballistic_Object(m=1,vx=0,vy=10,drag=0)
B.color = "b"

Solve(A,dt=0.01,tf=2.5)
Solve(B,dt=0.001,tf=2.5)

plt.figure("Ballistic")

plt.plot(A.list_t,A.list_y,f"{A.color}-")
plt.plot(A.list_t[-1],A.list_y[-1],f"{A.color}o")

plt.plot(B.list_t,B.list_y,f"{B.color}-")
plt.plot(B.list_t[-1],B.list_y[-1],f"{B.color}o")