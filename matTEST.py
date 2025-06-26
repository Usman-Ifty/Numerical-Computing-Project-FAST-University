import numpy as np
import matplotlib.pyplot as plt

B = 1

def f(r, N):
    return -2*N/r + 2/(3*r) - 4*B*r/3

def euler(f, r0, N0, h, rmax):
    r = r0
    N = N0
    rlist = [r0]
    Nlist = [N0]
    while r < rmax:
        N = N + h*f(r, N)
        r = r + h
        rlist.append(r)
        Nlist.append(N)
    print ("Value of N (up to 6 decimal places) at r = 5 is: ", round(N, 6))
    return rlist, Nlist

def rk4(f, r0, N0, h, rmax):
    r = r0
    N = N0
    rlist = [r0]
    Nlist = [N0]
    while r < rmax:
        k1 = h*f(r, N)
        k2 = h*f(r + h/2, N + k1/2)
        k3 = h*f(r + h/2, N + k2/2)
        k4 = h*f(r + h, N + k3)
        N = N + (k1 + 2*k2 + 2*k3 + k4)/6
        r = r + h
        rlist.append(r)
        Nlist.append(N)
    print("Value of N (up to 6 decimal places) at r = 5 is: ", round(N, 6))
    return rlist, Nlist

r0 = 0.1
N0 = 0.1

N = 10
h = round((5 - r0)/N, 6)
print("Step size: ", h)

rlist_euler, Nlist_euler = euler(f, r0, N0, h, 5)
rlist_rk4, Nlist_rk4 = rk4(f, r0, N0, h, 5)

plt.plot(rlist_euler, Nlist_euler, label='Euler')
plt.plot(rlist_rk4, Nlist_rk4, label='RK4')
plt.legend()
plt.grid()
plt.show()

data = np.array([rlist_rk4, Nlist_rk4])
np.savetxt('data_solution.txt', data, delimiter=',')
print("Data solution extracted and saved as data_solution.csv")

from scipy.interpolate import interp1d

f = interp1d(rlist_rk4, Nlist_rk4)
r = np.linspace(0.1, 5, 100)
N = f(r)

plt.plot(rlist_rk4, Nlist_rk4, 'o')
plt.plot(r, N)
plt.grid()
plt.show()
print("Solution set interpolated")