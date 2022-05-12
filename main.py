from Class import *
from Solver import Solve
import matplotlib.pyplot as plt

A = Ballistic_Object(y=1,m=1,drag=0)
B = Ballistic_Object(y=1,m=1,drag=0)
B.color = "b"

A.set_velocity(10,60)
B.set_velocity(10,30)

Solve(A,dt=0.01,tf=2.5)
Solve(B,dt=0.001,tf=2.5)

plt.figure("Ballistic")

plt.plot(A.list_x,A.list_y,f"{A.color}-")
plt.plot(A.list_x[-1],A.list_y[-1],f"{A.color}o")

plt.plot(B.list_x,B.list_y,f"{B.color}-")
plt.plot(B.list_x[-1],B.list_y[-1],f"{B.color}o")