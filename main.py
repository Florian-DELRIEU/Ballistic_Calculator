from Class import *
from Solver import Solve

A = Ballistic_Object(m=1,vx=1,vy=5,drag=1e-2)
B = Ballistic_Object(m=1,vx=1,vy=5,drag=1)
B.color = "b"

Solve(A,dt=0.01,tf=1)
Solve(B,dt=0.01,tf=1)
