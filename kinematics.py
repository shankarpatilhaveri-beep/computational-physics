#solver which plots the trajectory of a 1d particle with intial parameters like u and h given
import matplotlib.pyplot as plt
import numpy as np
def solvequadratic(a,b,c):
    disc = b**2-4*a*c
    if disc<0:
        return []
    if disc>=0:
        t1 = (-b+disc**0.5)/(2*a)
        t2 = (-b-disc**0.5)/(2*a)
    valid_list = []
    if t1>0:
        valid_list.append(t1)
    if t2>0:
        valid_list.append(t2)
    return valid_list
u = float(input("enter initial velocity with sign in m/s"))
h = float(input("enter the height of tower in m"))
g = 9.8
v = (u**2+2*g*h)**0.5
peak_time = u/g
peak_height = h+(u**2/(2*g))
result = solvequadratic(0.5*g,-u,-h)

if len(result) == 0:
    print("situation physically impossible")
else:
    times = np.linspace(0,max(result),10000)
    height = h+u*times-0.5*g*(times**2)
    
    plt.plot(times,height)
    plt.xlabel("Time in s")
    plt.ylabel("Height in m")
    if u>0:
        plt.scatter(peak_time,peak_height,color = "Red",label="max height")
        plt.text(peak_time,peak_height,f"max height = {peak_height:.2f}",ha="center",va="bottom")
    else:
        plt.scatter(0,h,color="Red",label="max height")
        plt.text(0,h,f"max height = {h:.2f}",ha="left",va="bottom")
    
    plt.scatter(max(result),0,color="Red",label="time of flight")
    plt.text(max(result),0,f"time of flight = {max(result):.2f}",ha="right",va="bottom") 
    plt.show()



        