from PyLTSpice import RawRead
import numpy as np
from matplotlib import pyplot as plt

# %% 1. RAW-Datei laden
LTR = RawRead(r"sim/Wien-VCO.raw")  # Erzeugte .raw-Datei aus LTSpice/NGSpice

print(LTR.get_trace_names())        # Alle Verwendeten Namen der Bauteile/ Knotenpunkte     

# Signale einlesen
Vd1 = LTR.get_trace("V(va)")
#Vd2 = LTR.get_trace("V(ve)") 
Vdstr = LTR.get_trace("V(vstr)")
time = LTR.get_trace("time") 
steps = LTR.get_steps()

v_ctrl_list = []
f_peak_list = []

print(f"Anzahl gefundener Simulationsschritte: {len(steps)}")

# %% Visualisierung & FFT-Berechnungen

# --- PLOT 1: Zeitbereich ---
plt.subplot(3, 2, (1,2))
for step in range(len(steps)):
    plt.plot(time.get_wave(step), Vd1.get_wave(step))
    #plt.plot(time.get_wave(step), Vd2.get_wave(step))

plt.grid()
plt.ylabel(r"Spannung in $V$")
plt.xlabel(r"Zeit in $s$")
plt.xlim(0,2.5e-6)

# --- PLOT 2: FFT Spektrum ---
plt.subplot(3, 2, (3,5))
for step in range(len(steps)):
    t = time.get_wave(step)
    vd1 = Vd1.get_wave(step)    # V(va)
    #vd2 = Vd2.get_wave(step)   # V(ve)
    
    n = len(t)
    t_uniform = np.linspace(t[0], t[-1], n)
    dt = t_uniform[1] - t_uniform[0] 

    vd1_uniform = np.interp(t_uniform, t, vd1)
    #vd2_uniform = np.interp(t_uniform, t, vd2)

    amp_vd1 = np.abs(np.fft.rfft(vd1_uniform)) * 2 / n
    #amp_vd2 = np.abs(np.fft.rfft(vd2_uniform)) * 2 / n
    freq = np.fft.rfftfreq(n, d=dt)

    plt.plot(freq[1:]/1000000, 20 * np.log10(amp_vd1[1:] + 1e-9))
    #plt.plot(freq[1:]/1000000, 20 * np.log10(amp_vd2[1:] + 1e-9))

plt.axvline(5.5, color="red", linestyle="--", label=r"Mittenfrequenz $5.5\,$MHz")
plt.axvline(5.0, color="orange", linestyle=":", label=r"Untere Grenzfrequenz $5.0\,$MHz")
plt.axvline(6.0, color="orange", linestyle=":", label=r"Obere Grenzfrequenz $6.0\,$MHz")
plt.xlim(4.8, 6.2)
plt.ylim(-80,20)

plt.legend()
plt.grid()
plt.ylabel(r"Amplitude in $dBV$")
plt.xlabel(r"Frequenz in $MHz$")

# --- Berechnungen für die VCO-Kennlinie ---
for step in range(len(steps)):
    t = time.get_wave(step)
    vd1 = Vd1.get_wave(step)

    n = len(t)
    t_uniform = np.linspace(t[0], t[-1], n)
    dt = t_uniform[1] - t_uniform[0] 

    vd1_uniform = np.interp(t_uniform, t, vd1)
    amp_vd1 = np.abs(np.fft.rfft(vd1_uniform)) * 2 / n
    freq = np.fft.rfftfreq(n, d=dt)

    vdstr_wave = Vdstr.get_wave(step)
    v_ctrl = np.mean(vdstr_wave) 
    v_ctrl_list.append(v_ctrl)

    # Peak-Frequenz oberhalb von 100 kHz bestimmen
    valid_range = np.where(freq > 100e3)[0]
    if len(valid_range) > 0:
        peak_idx = valid_range[np.argmax(amp_vd1[valid_range])]
        f_peak = freq[peak_idx]
    else:
        f_peak = 0
    f_peak_list.append(f_peak)

f_peak_mhz = np.array(f_peak_list) / 1e6
v_ctrl_np = np.array(v_ctrl_list) * 1000

# --- PLOT 3: VCO-Kennlinie ---
plt.subplot(3, 2, (4,6))
plt.plot(v_ctrl_np, f_peak_mhz, 'o-', color='green')
plt.xlabel(r"Steuerspannung $V_{str}$ in $mV$")
plt.ylabel(r"Frequenz in $MHz$")
plt.xlim(v_ctrl_np.min() * 0.95, v_ctrl_np.max() * 1.05)
plt.axhline(5, color="red", linestyle="--", label=r"Untere Frequenz $5.0\,$MHz")
plt.axhline(5.5, color="red", linestyle="--", label=r"Mittenfrequenz $5.5\,$MHz")
plt.axhline(6, color="red", linestyle="--", label=r"Obere Frequenz $6.0\,$MHz")
plt.grid()
plt.xlim(-50,1050)
plt.legend(loc="upper left")

plt.tight_layout()
plt.show()