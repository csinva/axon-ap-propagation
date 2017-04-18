import matplotlib.pyplot as plt
from matplotlib import rc
fig = plt.figure(figsize=(12, 7))
fig.set_facecolor('white')
rc('lines', markersize=4)
rc('legend', numpoints=1, fontsize=10)
rc('axes', labelsize=10)
rc('lines', markeredgewidth=0)
rc('axes', color_cycle=['#E24A33', '#348ABD', '#988ED5', '#777777', '#FBC15E',
                        '#8EBA42', '#FFB5B8', 'red', 'green', 'blue', 'purple', 'cyan', 'black', 'brown'])
rc('xtick', labelsize=7)
rc('ytick', labelsize=7)
plt.hold(True)
path = '/Users/chandansingh/drive/asdf/research/singh_connectome/'

import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'custom'
matplotlib.rcParams['mathtext.rm'] = 'Bitstream Vera Sans'
matplotlib.rcParams['mathtext.it'] = 'Bitstream Vera Sans:italic'
matplotlib.rcParams['mathtext.bf'] = 'Bitstream Vera Sans:bold'
plt.tight_layout()