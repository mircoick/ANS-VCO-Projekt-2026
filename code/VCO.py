from PyLTSpice import RawRead
import numpy as np
from matplotlib import pyplot as plt

LTR = RawRead("kicad/VCO-Schwingkreis/NET_VCO-Schwingkreis.raw")

print(LTR.get_trace_names())
print(LTR.get_raw_property())

Vd1 = LTR.get_trace("V(/drain_q1)")
Vd2 = LTR.get_trace("V(/drain_q2)") 
time = LTR.get_trace("time") 
steps = LTR.get_steps()
plt.subplot(2,1,1)
for step in range(len(steps)):
    plt.plot(time.get_wave(step) ,Vd1.get_wave(step), label=r"$V_{D1}$")
    plt.plot(time.get_wave(step) ,Vd2.get_wave(step), label=r"$V_{D2}$")



plt.legend()  # order a legend
plt.grid()
plt.ylabel(r"Voltage in $V$")
plt.xlabel(r"Time in $s$")

#--------------------------------------------------------------------------------------------------------------------------------
plt.subplot(2, 1, 2)

for step in range(len(steps)):
    t = time.get_wave(step)
    vd1 = Vd1.get_wave(step)
    vd2 = Vd2.get_wave(step)
    
    n = len(t)
    t_uniform = np.linspace(t[0], t[-1], n)
    dt = t_uniform[1] - t_uniform[0] 

    vd1_uniform = np.interp(t_uniform, t, vd1)
    vd2_uniform = np.interp(t_uniform, t, vd2)

    amp_vd1 = np.abs(np.fft.rfft(vd1_uniform)) * 2 / n
    amp_vd2 = np.abs(np.fft.rfft(vd2_uniform)) * 2 / n
    freq = np.fft.rfftfreq(n, d=dt)

    plt.semilogx(freq[1:], 20 * np.log10(amp_vd1[1:] + 1e-9), label=f"$V_{{D1}}$")
    plt.semilogx(freq[1:], 20 * np.log10(amp_vd2[1:] + 1e-9), label=f"$V_{{D2}}$")

plt.axvline(5.5e6, color="red", linestyle="--", label=r"Mittenfrequenz 5.5 MHz")
plt.xlim(4e6, 1e8) 

plt.legend()
plt.grid()
plt.ylabel(r"Amplitude in $dBV$")
plt.xlabel(r"Frequency in $Hz$")
plt.show()