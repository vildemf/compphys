from numpy import *
from matplotlib.pyplot import *

filename = open("gauss_test.txt", "r")

average = []
for line in filename:
    #line = line.split()
    average.append(float(line))

x = linspace(0, 1, 101)
print len(x)
print len(average)
plot(x[:], average[:])
#axis([0, 1, ])
show()

print average[:50]
