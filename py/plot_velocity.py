import numpy as np
import matplotlib.pyplot as plt
import plot_setup

fname = '../data/out.txt'
x = np.loadtxt(fname, skiprows=1)
headers = np.genfromtxt(fname, dtype="str")[0, :]
data = {}
for i in range(len(headers)):
    data[headers[i]] = x[:, i]
print("keys", data.keys())
ROWS=1
COLS=3
plt.subplot(ROWS,COLS,1)
plt.plot(data['nodal_diameter'], data['ave_velocity'])
plt.xlabel("Nodal Diameter")
plt.ylabel("AP Velocity")

plt.subplot(ROWS,COLS,2)
plt.plot(data['nodal_diameter'], data['na_flux'],label="Na flux")
plt.plot(data['nodal_diameter'], data['k_flux'],label="K flux")
plt.plot(data['nodal_diameter'], data['na_flux']+data['k_flux'],label="Total flux")
plt.xlabel("Nodal Diameter")
plt.ylabel("AP Costs")
plt.legend()

plt.subplot(ROWS,COLS,3)
plt.plot(data['ave_velocity'], data['na_flux'],label="Na flux")
plt.plot(data['ave_velocity'], data['k_flux'],label="K flux")
plt.plot(data['ave_velocity'], data['na_flux']+data['k_flux'],label="Total flux")
plt.xlabel("AP Velocity")
plt.ylabel("AP Costs")
plt.legend()

plt.savefig("../plots/energy_velocity_diameter.pdf")
plt.show()
