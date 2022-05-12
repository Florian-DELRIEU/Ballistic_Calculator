from Class import *
from Solver import Solve
import matplotlib.pyplot as plt

Stuka_velocity = 400 / 3.6
Stuka_angle =  -45

bombe_50 = Ballistic_Object(m=50,y=1400,drag=0.1)
bombe_50.set_velocity(Stuka_velocity,Stuka_angle)
bombe_50.color = "b"

bombe_100 = Ballistic_Object(m=100,y=1400,drag=0.12)
bombe_100.set_velocity(Stuka_velocity,Stuka_angle)
bombe_100.color = "r"

print("running 50kg ...")
Solve(bombe_50,dt=0.01,tf=100)
print(f"La bombe percute le sol après {bombe_50.list_t[-1]} secondes")

print("running 100kg ...")
Solve(bombe_100,dt=0.01,tf=100)
print(f"La bombe percute le sol après {bombe_50.list_t[-1]} secondes")

plt.figure("Ballistic")

plt.plot(bombe_50.list_x,bombe_50.list_y,f"{bombe_50.color}-",label ='50 kg')
plt.plot(bombe_50.list_x[-1],bombe_50.list_y[-1],f"{bombe_50.color}o")

plt.plot(bombe_100.list_x,bombe_100.list_y,f"{bombe_100.color}-",label="100 kg")
plt.plot(bombe_100.list_x[-1],bombe_100.list_y[-1],f"{bombe_100.color}o")
plt.legend(loc="best")
