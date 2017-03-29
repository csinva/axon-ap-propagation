import numpy as np
import matplotlib.pyplot as plt
import plot_setup

fname = '../data/Dbl_Taper_20uDF_1.txt'
x = np.loadtxt(fname, skiprows=1)
headers = np.genfromtxt(fname, dtype="str")[0, :]
data = {}
for i in range(len(headers)):
    data[headers[i]] = x[:, i]
plt.plot(data['nodal_diameter'], data['ave_velocity'])
plt.xlabel("Nodal Diameter")
plt.ylabel("Velocity")
plt.savefig("../plots/velocity.pdf")
plt.show()
