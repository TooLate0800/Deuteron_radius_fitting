import numpy as np
import matplotlib.pyplot as plt
import argparse
from scipy import constants
from scipy.misc import derivative
_m_e = constants.value('electron mass energy equivalent in MeV') * 1e-3
_mu_p = constants.value('proton mag. mom. to nuclear magneton ratio')
_m_p = constants.value('proton mass energy equivalent in MeV') * 1e-3
_m_d = constants.value('deuteron mass energy equivalent in MeV') * 1e-3
_m2_e = _m_e**2
_alpha = constants.alpha
_inv_fm_to_gev = constants.hbar * constants.c / constants.e * 1e6  # fm^{-1} to GeV
_gev_to_inv_fm = 1 / _inv_fm_to_gev
_inv_gev_to_fm = _inv_fm_to_gev
_inv_gev_to_mkb = _inv_gev_to_fm**2 * 1e4
Mp = 938.272046
tofm = 25.68189504

#Load txt file
data1 = np.loadtxt('cs_bin_errors_1100_new.txt', float)
data2 = np.loadtxt('cs_bin_errors_2200_new.txt', float)
Theta1 = data1[:,0]
Theta2 = data2[:,0]
xs1 = data1[:,1]
xs2 = data2[:,1]
dxs1 = data1[:,2]/np.sqrt(3)
dxs2 = data2[:,2]/np.sqrt(7)
#=========functions
def mott(ei_e, theta_e):
    cos_theta_2 = np.cos(theta_e / 2)
    sin2_theta_2 = 1 - cos_theta_2**2
    return (_alpha * cos_theta_2 / (2 * ei_e * sin2_theta_2))**2 * _inv_gev_to_mkb
def get_ef(ei_e, theta_e, m_h):
    sin_theta = np.sin(theta_e)
    cos_theta = np.cos(theta_e)
    return ((ei_e + m_h) * (ei_e * m_h + _m2_e) + np.sqrt(m_h**2 - _m2_e * sin_theta**2) *
            (ei_e**2 - _m2_e) * cos_theta) / ((ei_e + m_h)**2 - (ei_e**2 - _m2_e) * cos_theta**2)
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

# Radius
#def f(q2):
#    return int_ia(q2)
#ax = derivative(f, 0.001, dx = 1e-4)
##ax = derivative(f, 0.000001, dx = 1e-6)
#R = np.sqrt(-6*ax)
#print(R)
#===========generator loops======================
i = 1
N = 10000
N1 = 30
N2 = 37
while i <= N:
    j = 0
    k = 0
    l = str(i)
    #with open('1GeV_IA.txt', 'w') as f:
    with open('iamec/1GeV_smear_cs_' + l + '.txt', 'w') as f:
        f.write(f'%d\n'%N1)
        while j< N1:
            ei = 1.1
            theta = Theta1[j] * np.pi / 180
            ef = get_ef(ei, theta, _m_d)
            q2 = 4 * ei * ef * np.sin(theta / 2)**2
            q2 = q2 * _gev_to_inv_fm**2
            mot = mott(ei, theta) * ef / ei
            da = dxs1[j] / mot
            gc=int_iamec(q2)
            dgc = da / (2 * gc)
            ggc = gc+np.random.normal(0.0,dgc)
            #ggc = gc
            f.write(f'{q2:8.6f} {ggc:8.6f} {dgc:8.6f}\n')
            j += 1
    #with open('2GeV_IA.txt', 'w') as g:
    with open('iamec/2GeV_smear_cs_' + l + '.txt', 'w') as g:
        g.write(f'%d\n'%N2)
        while k < N2:
            ei = 2.2
            theta = Theta2[k] * np.pi / 180
            ef = get_ef(ei, theta, _m_d)
            q2 = 4 * ei * ef * np.sin(theta / 2)**2
            q2 = q2 * _gev_to_inv_fm**2
            mot = mott(ei, theta) * ef / ei
            da = dxs2[k] / mot
            gc=int_iamec(q2)
            dgc = da / (2 * gc)
            ggc = gc*(1+np.random.normal(0.0,dgc))
            #ggc = gc
            g.write(f'{q2:8.6f} {ggc:8.6f} {dgc:8.6f}\n')
            k += 1
    i += 1

