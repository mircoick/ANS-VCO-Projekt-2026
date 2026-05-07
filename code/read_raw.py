import numpy as np
from matplotlib import pyplot as plt
from PyLTSpice import RawRead

LTR = RawRead("../kicad/nnmoos/NMOS.raw")
step = 0 

x_vals = np.array(LTR.get_trace('v(v-sweep)').get_wave(step))
i_vals = np.array(LTR.get_trace('i(xq1:1)').get_wave(step))
u_vals = np.array(LTR.get_trace('v(/vg)').get_wave(step))

print(LTR.get_trace_names())
print(u_vals)

idx_nullen = np.where(x_vals == 0)[0]

x_teile = np.split(x_vals, idx_nullen)
i_teile = np.split(i_vals, idx_nullen)

print(f"{len(x_teile)} Kennlinien")

for k in range(len(x_teile)):
    plt.plot(x_teile[k], i_teile[k], label=f"Kennlinie {k+1}")
    #i_teile[k][-1]

plt.legend()
plt.xlabel(r"$U_{DS}$ in V")
plt.ylabel(r"$I_D$ in A")
plt.grid()
plt.show()
