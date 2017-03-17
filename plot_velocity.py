import numpy as np
import matplotlib.pyplot as plt

x = np.loadtxt('Dbl_Taper_20uDF.txt', skiprows=1)
headers = np.genfromtxt('Dbl_Taper_20uDF.txt', dtype="str")[0, :]
data = {}
for i in range(len(headers)):
    data[headers[i]] = x[:, i]
print(x)
plt.plot(data['Dn'], data['ave_velocity'])
plt.xlabel("Dn")
plt.ylabel("ave_velocity")
plt.show()
