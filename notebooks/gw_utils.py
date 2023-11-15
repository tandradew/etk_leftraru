import os

import numpy as np
from scipy.fftpack import fft, ifft, fftfreq
from scipy.signal import find_peaks

import matplotlib.pyplot as plt

###########################################################
# get puncture trajectories 
###########################################################

def get_trajectories(path):
    
    ascii_grid = np.loadtxt(f'{path}puncturetracker-pt_loc..asc')

    idx = [8, 22, 23, 32, 33, 42, 43]
    cols = ['t', 'x1', 'x2', 'y1','y2','z1','z2']
    id_dict = dict(zip(cols, idx))

    t = ascii_grid[:,id_dict['t']]
    trajectory1 = ascii_grid[:,id_dict['x1']], ascii_grid[:,id_dict['y1']]
    trajectory2 = ascii_grid[:,id_dict['x2']], ascii_grid[:,id_dict['y2']]
    
    return t, trajectory1, trajectory2 

###########################################################
# get psi4
###########################################################
    
def read_psi4(path, r, lm = (2,2)):
    
    l,m = lm
    gw_data = np.loadtxt(f'{path}mp_psi4_l{l}_m{m}_r{r}.asc')
    
    t = gw_data[:,0]
    re_psi4 = gw_data[:,1]
    im_psi4 = gw_data[:,2]
    
    psi4 = float(r)*np.array(re_psi4 + 1j*im_psi4)
    
    return t, psi4

###########################################################
# Fixed frequency integration
###########################################################

def calc_ffi(path, r, lm = (2,2), kind = 'strain', f0 = 0.01):
    
    """
    computation of FFI for strain and hdot
    
    Parameters
       - path
       - r: radius
       - 
    """

    t, psi4_data = read_psi4(path, r, lm = lm)
    dt = t[1] - t[0]

    if kind == 'hdot':
        signal = fixed_freq_int_n(psi4_data, f0, order = 1, dt=dt)

    if kind == 'strain':
        signal = fixed_freq_int_n(psi4_data, f0, order = 2, dt=dt)

    return t, signal


def fixed_freq_int_n(signal, cutoff, order=2, dt=1):
    """
    Fixed frequency time integration
    
    * signal : a np array with the target signal
    * cutoff : the cutoff frequency
    * order  : number of time integrations
    * dt     : the sampling of the signal
    """
    
    f = fftfreq(signal.shape[0], dt)

    idx_p = np.logical_and(f >= 0, f < cutoff)
    idx_m = np.logical_and(f <  0, f > -cutoff)

    f[idx_p] = cutoff
    f[idx_m] = -cutoff

    D0 = -1j/(2*np.pi*f)
    
    return ifft( D0**order * fft(signal))

###################################################################
### get ADM parameters
###################################################################

def get_ADM_param(path):
    
    file_name = path+'quasilocalmeasures-qlm_scalars..asc'
    qlm = np.loadtxt(file_name)
    
    # 69:qlm_mass[2]
    # 66:qlm_coordspinz[2]
    M_f = qlm[-1,69-1]
    J_f = qlm[-1,66-1]
    
    # TwoPunctures.bbh
    f = open(path+'TwoPunctures.bbh', "r")
    lines = f.read().split('\n')

    # initial separation
    D = find_param(lines, 'initial-separation')

    # initial ADM quantities
    M_i = find_param(lines, 'initial-ADM-energy')
    J_i = find_param(lines, 'initial-ADM-angular-momentumz')

    # initial puncture bare masses
    #m1_i = find_param(lines,'initial-bh-puncture-bare-mass1')
    #m2_i = find_param(lines,'initial-bh-puncture-bare-mass2')
    
    output = {'M_i': M_i, 'J_i': J_i, 'M_f': M_f, 'J_f': J_f, 'D': D}
    
    return output

def find_param(lines, unique_match):
    line = [l for l in lines if unique_match in l][0]
    return float(line.split('=')[-1])
