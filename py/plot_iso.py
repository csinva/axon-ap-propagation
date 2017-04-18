import numpy as np
import matplotlib.pyplot as plt
import setup


def plot_filter(x, y, filter="nodal_length", filter_value=1):
    idxs = data[filter] == filter_value
    plt.plot(x[idxs], y[idxs], label=filter + "=" + str(filter_value))


nodal_lengths = [.6, 1, 1.4, 1.8]
base_dir = "/Users/chandansingh/drive/asdf/research/act_potential"
fname = base_dir + '/data/nodal_diameter,nodal_length.txt'
x = np.loadtxt(fname, skiprows=1)
headers = np.genfromtxt(fname, dtype="str")[0, :]
data = {}
for i in range(len(headers)):
    data[headers[i]] = x[:, i]
print("keys", data.keys())
print(np.unique(data['nodal_length']))
ROWS = 1
COLS = 3
plt.subplot(ROWS, COLS, 1)
for nodal_length in nodal_lengths:
    plot_filter(data["nodal_diameter"] * data["nodal_length"] * 3.14159, data["ave_velocity"], filter="nodal_length",
                filter_value=nodal_length)
plt.xlabel("Nodal Surface Area")
plt.ylabel("AP Velocity")
# plt.legend()

plt.subplot(ROWS, COLS, 2)
for nodal_length in nodal_lengths:
    # plt.plot(data['nodal_diameter'], data['na_flux'], label="Na flux")
    # plt.plot(data['nodal_diameter'], data['k_flux'], label="K flux")
    plot_filter(data["nodal_diameter"] * data["nodal_length"] * 3.14159, data["na_flux"] + data["k_flux"], filter="nodal_length",
                filter_value=nodal_length)
plt.xlabel("Nodal Surface Area")
plt.ylabel("AP Costs")
# plt.legend()

plt.subplot(ROWS, COLS, 3)
for nodal_length in nodal_lengths:
    # plt.plot(data['ave_velocity'], data['na_flux'], label="Na flux")
    # plt.plot(data['ave_velocity'], data['k_flux'], label="K flux")
    plot_filter(data["ave_velocity"], data["na_flux"] + data["k_flux"], filter="nodal_length",
                filter_value=nodal_length)
plt.xlabel("AP Velocity")
plt.ylabel("AP Costs")
plt.legend()

plt.savefig(base_dir + "/plots/energy_velocity_diameter_iso.pdf")
plt.show()
