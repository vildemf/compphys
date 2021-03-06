from numpy import *
from matplotlib.pyplot import *

"""
Plot:
Difflinkningene:
Rel er: 3x 2-delt subplot (3 metoder, 2 delta x)
Velg ut beste metode, 1 plot med 4 tidspunkt-grafer
"""


infile = open("reler.txt", 'r')

parameters = infile.readline()
v_num = []

for line in infile:
    line = line.split()
    v_num.append(float(line[1]))

#x = linspace(0, 1, 201)
t = linspace(0, 0.5, 50000)
def v_an(T):
    #T=0.5
    x = 0.5
    v = 0
    for n in range(1,50):
        v += (1./n)*sin(n*pi*x)*exp(-T*(n*pi)**2)
    v *= -2/pi
    return v

x = 0.5
u_num=array(v_num) + 1 - x
u_an=array(v_an(t)) + 1 - x

#plot(x,u_num, x, u_an)
#plot(t[5000:], abs((u_an-u_num)/u_an)[5000:])
semilogy(t, abs((u_an-u_num)))
#plot(t, u_an, t, u_num)
#legend(["Analytical","Numerical"])
#legend(["Numerical", "Analytic"])

override = {
    'fontsize'            : 'large',
    'verticalalignment'   : 'baseline',
    'horizontalalignment' : 'center'
    }
xlabel("x", override)
ylabel("Relative error $\\times$1E-6", override)
title("Explicit Forward Euler Relative Error \n T=0.5 Nt=5000 Nx=200")
show()
"""
ylabel("v(x, t=5")
title("Explicit Forward Euler \n Nx=20 Nt=5000")
show()
"""
