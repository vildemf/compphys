from numpy import *
from matplotlib.pyplot import *

infile = open("crank.txt", 'r')
parameters = infile.readline()
v_num = []

for line in infile:
    v_num.append(float(line))

x = linspace(0, 1, 201)

def u_analytic(x):
    T=0.3
    v = 0
    for n in range(1,200):
        v += (1./n)*sin(n*pi*x)*exp(-T*(n*pi)**2)
    v *= -2/pi
    return array(v)+1-x


u_num=array(v_num) + 1 - x
u_an=u_analytic(x)

plot(x,u_num, x, u_an)
legend(["Numerical", "Analytic"])
override = {
    'fontsize'            : 'large',
    'verticalalignment'   : 'baseline',
    'horizontalalignment' : 'center'
    }
xlabel("x", override)
ylabel("u(x, t=T)", override)
title("Explicit Forward Euler \n Nt=5000 Nx=200")
show()

