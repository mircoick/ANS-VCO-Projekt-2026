import numpy as np
import PyLTSpice as lt
from matplotlib import pyplot as plt

LTR = lt.RawRead("./Testprojekt/NMOS.raw")

Id_raw = np.array(LTR.get_trace("I(XQ1:1)"))
Vgs_raw = np.array(LTR.get_trace("V(/vg)"))
Vds_raw = np.array(LTR.get_trace("V(/vd)"))

break_indices = np.where(np.diff(Vgs_raw) < 0)[0] + 1
starts = np.insert(break_indices, 0, 0)
ends = np.append(break_indices, len(Vgs_raw))

all_measurements = []

plt.figure(figsize=(12, 8))

for i in range(len(starts)):
    vgs_slice = Vgs_raw[starts[i]:ends[i]]
    id_slice = Id_raw[starts[i]:ends[i]]
    
    all_measurements.append({'Vgs': vgs_slice, 'Id': id_slice})
    
    plt.plot(vgs_slice, id_slice, label=f'$V_{{DD}} = {i}V$')

plt.xlabel('$V_{DS}$ in V')
plt.ylabel('$I_D$ in A')
plt.title('Transistorkennlinie')
plt.legend()
plt.grid()
plt.show()