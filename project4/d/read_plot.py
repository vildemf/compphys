import numpy as np
import matplotlib.pyplot as plt

f = "PE_L20t1t24.txt"
data_file = open(f, 'r')

L          = []
number_mcs = []
time       = []
temp       = []
E_exp      = []
M_exp      = [] # |<M>|
M_abs_exp  = [] # <|M|>
Cv         = []
chi        = []
chi_abs    = []
accepted_counter = []
Evariance = []
Et1 = []#{}
Et24 = []#{}

i = 1
for line in data_file:
    line = line.split()
    if i==1 or i==3:
        L.append(float(line[0]))
        number_mcs.append(float(line[1]))
        time.append(float(line[2]))
        temp.append(float(line[3]))
        E_exp.append(float(line[4]))
        M_exp.append(float(line[5]))
        M_abs_exp.append(float(line[6]))
        Cv.append(float(line[7]))
        chi.append(float(line[8]))
        chi_abs.append(float(line[9]))
        accepted_counter.append(float(line[10]))
        Evariance.append(float(line[11]))
    if i==2:
        for j in range(len(line)):
            Et1.append(float(line[j]))
            """
            if float(line[j])!=0:
                # j-800(key)=energy, Et1[j](element)=count
                Et1[j-800] = float(line[j])  
            """
    if i==4:
        for j in range(len(line)):
            Et24.append(float(line[j]))
            """
            if float(line[j])!=0:
                # j-800(key)=energy, Et24[j](element)=count
                Et24[j-800] = float(line[j])  
            """
    i+=1
                
n_mcs = number_mcs[0]
L = L[0]
energies = np.linspace(-2*L*L, 2*L*L, len(Et1))

Et1 = np.array(Et1)/n_mcs
Et24 = np.array(Et24)/n_mcs
print sum(Et1)
print sum(Et24)

print Evariance

plt.figure(1)
plt.subplot(211)
plt.plot(energies, Et24)
plt.ylabel("P(E)")
plt.legend(["T=2.4"])
plt.title("P(E) at L=20")

plt.subplot(212)
plt.plot(energies, Et1, 'r')
plt.axis([-810, 800, 0, 0.9])
plt.legend(["T=1.0"])
plt.xlabel("E")
plt.show()

"""
plt.figure(1)
plt.subplot(211)
plt.plot(n_mcs, count3, 'ro-')
plt.title("Number of accepted spin flips\nL=20")
plt.legend(["T=3\ninit. config.=random"], loc=4)
plt.grid()

plt.subplot(212)
plt.plot(n_mcs, count2, 'go-')
plt.ylabel("Number of accepted moves")
plt.legend(["T=2\ninit. config.=random"], loc=4)
plt.grid()

plt.xlabel("log10(Time [number of MC cycles])")
plt.show()
"""
