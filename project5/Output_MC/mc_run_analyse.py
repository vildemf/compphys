from numpy import *
from matplotlib.pyplot import *
from os import system

dt = "0.00005"

mc_number = 1E7
#cpp_program = "build-diffusion_mc-Desktop_Qt_5_4_1_GCC_64bit-Debug/diffusion_mc"
cpp_program = "build-diffusion_mc_gauss-Desktop_Qt_5_4_1_GCC_64bit-Debug/diffusion_mc_gauss"


def u_analytical(x, t):
    v = 0
    for n in range(1,50):
        v += (1./n)*sin(n*pi*x)*exp(-t*(n*pi)**2)
    v *= -2/pi
    u = array(v) + 1 - x
    return u

def plot_relerror():
    T = "0.3"
    T1 = T.split('.')[0]
    T2 = T.split('.')[1]
    dt1 = dt.split('.')[0]
    dt2 = dt.split('.')[1]
    filename = "/home/vilde/Documents/FYS3150/project5/mcgauss_errT%sp%sdt%sp%sMCn%d" % (T1, T2, dt1, dt2, mc_number)
    #print filename
    Tf=float(T)
    dtf = float(dt)
    Nt = round(Tf/dtf)+1
    system("./%s %s %f %f %d" % \
           (cpp_program, filename, Tf, dtf, mc_number))
    
    d=1
    D=1
    l0 = sqrt(2*D*dtf)
    #Nx = round(d/l0 + 1)
    Nx = 100
    x = linspace(0, d, Nx+1)
    datafile = open(filename)
    u_an = u_analytical(x, Tf)
    u = []
    for line in datafile:
        u.append(float(line))
    u = array(u)
    err = abs(u_an-u)/u_an
    plot(x, err)
    #legends.append("T=%.3f $N_t$=%d" % (Tf, Nt))

    override = {
        'fontsize'            : 'large',
        'verticalalignment'   : 'baseline',
        'horizontalalignment' : 'center'
    }
    xlabel("x", override)
    ylabel("Relative error", override)
    title("Monte Carlo, continuous, error \n T=%.1f $\\Delta t$=%.4f $l_0$=%.2f $N_{MC}$=%.0E" % (Tf,dtf, l0, mc_number) )
    #legend(legends)
    show()
#plot_relerror()



def plot_result():
    legends=[]
    Tlist = ["0.3"]#, "0.01", "0.08", "0.3"]
    for T in Tlist:
        T1 = T.split('.')[0]
        T2 = T.split('.')[1]
        dt1 = dt.split('.')[0]
        dt2 = dt.split('.')[1]
        #filename = "/home/vilde/Documents/FYS3150/project5/mc_T%sp%sdt%sp%sMCn%d.txt" % (T1, T2, dt1, dt2, mc_number)
        filename = "/home/vilde/Documents/FYS3150/project5/mcgauss_T%sp%sdt%sp%sMCn%d.txt" % (T1, T2, dt1, dt2, mc_number)
        print filename
        Tf=float(T)
        dtf = float(dt)
        Nt = round(Tf/dtf)+1
        #system("./%s %s %f %f %d" % \
        #       (cpp_program, filename, Tf, dtf, mc_number))
        
        d=1
        D=1
        l0 = sqrt(2*D*dtf)
        #Nx = round(d/l0 + 1)
        Nx = 100
        x = linspace(0, d, Nx+1)
        datafile = open(filename)
        u = []
        for line in datafile:
            u.append(float(line))
        plot(x, u, 'ro')
        legends.append("T=%.3f $N_t$=%d" % (Tf, Nt))

    override = {
        'fontsize'            : 'large',
        'verticalalignment'   : 'baseline',
        'horizontalalignment' : 'center'
    }
    xlabel("x", override)
    ylabel("u(x, t=T)", override)
    title("Monte Carlo, continuous position \n T=0.3 $\\Delta t$=%.4f $l_0=\\xi\\sqrt{2D\\Delta t}$ $N_{MC}$=%.0E" % (dtf, mc_number) )
    #legend(legends)
    axis([-0.1, 0.5, 0.5, 1.3])
    show()
plot_result()
