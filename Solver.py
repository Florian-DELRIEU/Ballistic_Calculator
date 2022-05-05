from Class import *
from numpy import abs

def Solve(A=Ballistic_Object(), dt=0.1, tf=100):
    t = 0
    print("running ...")
    while t <= tf:
        A.ax = ( -1/2*Rho*A.surface*abs(A.vx)*A.drag_coefficient*A.vx       ) / A.mass
        A.ay = ( -1/2*Rho*A.surface*abs(A.vy)*A.drag_coefficient*A.vy - g   ) / A.mass

        A.vx += A.ax*dt
        A.vy += A.ay*dt

        A.x += A.vx*dt
        A.y += A.vy*dt

        t += dt