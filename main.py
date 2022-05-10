from Class import *
from Solver import Solve

A = Ballistic_Object(m=1,vx=0,vy=10,drag=0)

Solve(A,dt=0.01,tf=2.5)