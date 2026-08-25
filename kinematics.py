#solver which plots the trajectory of a 1d particle with intial parameters like u and h given
import matplotlib.pyplot as plt
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
heights = []
times = []
t=0.00
if len(result) == 0:
    print("situation physically impossible")
else:
    while t<=max(result):
        Y = h + u*t - 0.5*g*t*t
        heights.append(Y)
        times.append(t)
        t += 0.1
    times.append(max(result))
    heights.append(0)
    
    plt.plot(times,heights)
    plt.xlabel("Time in s")
    plt.ylabel("Height in m")
    plt.scatter(u/g,h+(u**2/(2*g)),color = "Red",label="max height")
    plt.scatter(max(result),0,color="Red",label="time of flight")
    plt.text(peak_time,peak_height+0.01,f"max height = {peak_height:.2f}",ha="right",va="bottom")
    plt.text(max(result)-0.1,0,f"time of flight = {max(result):.2f}",ha="right",va="bottom")
    plt.show()



        