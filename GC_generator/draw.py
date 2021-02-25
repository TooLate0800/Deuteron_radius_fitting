import numpy as np
import matplotlib.pyplot as plt
import argparse
from scipy import constants
from scipy.misc import derivative


#==========Deuteron form factors
def abbott_2000_1(q2, *args, **kwargs):
    # Parameterization I in Eur. Phys. J A 7(2000)421
    # r_0 = 2.094
    gc0, qc0 = 1, 4.21
    gm0, qm0 = 1.714, 7.37
    gq0, qq0 = 25.83, 8.1
    ac = [0, 6.740e-1, 2.246e-2, 9.806e-3, -2.709e-4, 3.793e-6]
    am = [0, 5.804e-1, 8.701e-2, -3.624e-3, 3.448e-4, -2.818e-6]
    aq = [0, 8.796e-1, -5.656e-2, 1.933e-2, -6.734e-4, 9.438e-6]
    gc = gc0 * (1 - q2 / qc0**2) / (1 + sum([ac[i] * q2**i for i in range(1, 6)]))
    gm = gm0 * (1 - q2 / qm0**2) / (1 + sum([am[i] * q2**i for i in range(1, 6)]))
    gq = gq0 * (1 - q2 / qq0**2) / (1 + sum([aq[i] * q2**i for i in range(1, 6)]))
    return gc, gm, gq
def abbott_2000_2(q2, *args, **kwargs):
    # Parameterization II in Eur. Phys. J A 7(2000)421
    # r_0 = 2.088
    eta = q2 / (4 * (_m_d * _gev_to_inv_fm)**2)
    delta = (0.89852 * _gev_to_inv_fm)**2
    gq2 = 1 / (1 + q2 / (4 * delta))**2
    a = [1.57057, 12.23792, -42.04576, 27.92014]
    alpha = [1.52501, 8.75139, 15.97777, 23.20415]
    b = [0.07043, 0.14443, -0.27343, 0.05856]
    beta = [43.67795, 30.05435, 16.43075, 2.80716]
    c = [-0.16577, 0.27557, -0.05382, -0.05598]
    gamma = [1.87055, 14.95683, 28.04312, 41.12940]
    g0 = sum([a[i] / (alpha[i] + q2) for i in range(4)])
    g1 = numpy.sqrt(q2) * sum([b[i] / (beta[i] + q2) for i in range(4)])
    g2 = q2 * sum([c[i] / (gamma[i] + q2) for i in range(4)])
    C = gq2**2 / (2 * eta + 1)
    sqrt_2_eta = numpy.sqrt(2 * eta)
    gc = C * ((1 - 2 / 3 * eta) * g0 + 8 / 3 * sqrt_2_eta * g1 + 2 / 3 * (2 * eta - 1) * g2)
    gm = C * (2 * g0 + 2 * (2 * eta - 1) / sqrt_2_eta * g1 - 2 * g2)
    gq = C * (-1 * g0 + 2 / sqrt_2_eta * g1 - (1 + 1 / eta) * g2)
    return gc, gm, gq
def dipole(q2, *args, **kwargs):
    r = 2.088
    gc = 1 / (1 + q2 * r**2 / 12)**2
    return gc
def monopole(q2, *args, **kwargs):
    r = 2.088
    gc = 1 / (1 + q2 * r**2 / 6)
    return gc
def gaussian(q2, *args, **kwargs):
    r = 2.088
    gc = 1 * numpy.exp(-q2 * r**2 / 6)
    return gc
def F_quadratic_10points(q2, *args, **kwargs):
    x = q2/tofm
    gc = 1 -15.701*x+106.05*x**2
    return gc
def F_cubic_10points(q2, *args, **kwargs):
    x = q2/tofm
    gc = 1 -18.318*x+229.76*x**2-1372.6*x**3
    return gc

# Load The Hummel and Tjon Parameterizations

ia=np.loadtxt("ia.fc")
iamec=np.loadtxt("iamec.fc")
rsc=np.loadtxt("rsc.fc")
rscmec=np.loadtxt("rscmec.fc")


# Interpolate the Hummel and Tjon Parameterizations

from scipy.interpolate import interp1d
int_ia=interp1d(ia[:,0],ia[:,1],kind='cubic')
int_iamec=interp1d(iamec[:,0],iamec[:,1],kind='cubic')
int_rsc=interp1d(rsc[:,0],rsc[:,1],kind='cubic')
int_rscmec=interp1d(rscmec[:,0],rscmec[:,1],kind='cubic')

myq2=np.linspace(0,0.001,1000)
gc_ia = int_ia(myq2)
gc_R11_ia = (1-0.07869*myq2)/(1+0.68601*myq2)
gc_R13_ia = (1-0.02246*myq2)/(1+0.74256*myq2+0.0416*myq2**2+0.00474*myq2**3)
gc_iamec = int_iamec(myq2) 
gc_R11_iamec = (1-0.07775*myq2)/(1+0.68658*myq2)
gc_R13_iamec = (1-0.02143*myq2)/(1+0.74324*myq2+0.0416*myq2**2+0.00474*myq2**3)
gc_rsc = int_rsc(myq2)
gc_R11_rsc = (1-0.07023*myq2)/(1+0.66263*myq2)
gc_R13_rsc = (1-0.01094*myq2)/(1+0.72234*myq2+0.0416*myq2**2+0.00474*myq2**3)
gc_rscmec = int_rscmec(myq2)
gc_R11_rscmec = (1-0.06942*myq2)/(1+0.66309*myq2)
gc_R13_rscmec = (1-0.01004*myq2)/(1+0.72289*myq2+0.0416*myq2**2+0.00474*myq2**3)
#
#plt.semilogx(myq2,gc_ia,c = 'black')
#plt.semilogx(myq2,gc_R11_ia,c = 'red')
#plt.semilogx(myq2,gc_R13_ia,c = 'blue')
#plt.xscale('symlog')
plt.plot(myq2,gc_ia,c = 'black')
plt.plot(myq2,gc_iamec,c = 'grey')
plt.plot(myq2,gc_rsc,c = 'red')
plt.plot(myq2,gc_rscmec,c = 'salmon')
plt.savefig("graph.png")
#print(gc)
