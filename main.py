from Class import *
from Solver import Solve

A = Ballistic_Object(m=1,vx=1,vy=5)

print(f"""
Initial speed : {A.V} m/s
Initial position: x = {A.x} , y = {A.y}
""")

input("Press a key to run solver ... ")

Solve(A,dt=0.1,tf=1)

print(f"""
Final speed : {A.V} m/s
Final position: x = {A.x} , y = {A.y}
""")