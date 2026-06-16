from PyLTSpice import RawRead
import numpy as np
from matplotlib import pyplot as plt

# %% 1. RAW-Datei laden
LTR = RawRead(r"../kicad/Wien-Brücken-VCO_5MHz5/Wien-LT.raw")

print(LTR.get_trace_names())
print(LTR.get_raw_property())

Vd1 = LTR.get_trace("V(va)")
Vd2 = LTR.get_trace("V(ve)") 
Vdstr = LTR.get_trace("V(vstr)")

print(Vdstr)
time = LTR.get_trace("time") 
steps = LTR.get_steps()

# %% Auswertung transienter Spannungsverläufe und Frequenzspektren
plt.subplot(3, 1, 1)

for step in range(len(steps)):
    plt.plot(time.get_wave(step), Vd1.get_wave(step))
    plt.plot(time.get_wave(step), Vd2.get_wave(step))

# plt.legend()  # order a legend
plt.grid()
plt.ylabel(r"Voltage in $V$")
plt.xlabel(r"Time in $s$")

# %% Spektren der Ausgangsspannungen V(va) und V(ve) über alle Simulationsschritte hinweg
plt.subplot(3, 1, 2)

for step in range(len(steps)):
    t = time.get_wave(step)
    vd1 = Vd1.get_wave(step)  # V(va)
    vd2 = Vd2.get_wave(step)  # V(ve)
    
    n = len(t)
    t_uniform = np.linspace(t[0], t[-1], n)
    dt = t_uniform[1] - t_uniform[0] 

    vd1_uniform = np.interp(t_uniform, t, vd1)
    vd2_uniform = np.interp(t_uniform, t, vd2)

    amp_vd1 = np.abs(np.fft.rfft(vd1_uniform)) * 2 / n
    amp_vd2 = np.abs(np.fft.rfft(vd2_uniform)) * 2 / n
    freq = np.fft.rfftfreq(n, d=dt)

    plt.semilogx(freq[1:], 20 * np.log10(amp_vd1[1:] + 1e-9))
    plt.semilogx(freq[1:], 20 * np.log10(amp_vd2[1:] + 1e-9))

plt.axvline(5.5e6, color="red", linestyle="--", label=r"Mittenfrequenz 5.5 MHz")
plt.axvline(5.0e6, color="orange", linestyle=":", label=r"Untere Grenzfrequenz 5.0 MHz")
plt.axvline(6.0e6, color="orange", linestyle=":", label=r"Obere Grenzfrequenz 6.0 MHz")
plt.xlim(4e6, 8e6) 

plt.legend()
plt.grid()
plt.ylabel(r"Amplitude in $dBV$")
plt.xlabel(r"Frequency in $Hz$")

# %% VCO-Kennlinie: Steuerspannung V(vstr) vs. Frequenz der Ausgangsspannung V(va)
Vd1 = LTR.get_trace("V(va)")
time = LTR.get_trace("time") 
steps = LTR.get_steps()

v_ctrl_list = []
f_peak_list = []

print(f"Anzahl gefundener Simulationsschritte: {len(steps)}")

# Schleife über alle Simulationsschritte
for step in range(len(steps)):
    t = time.get_wave(step)
    vd1 = Vd1.get_wave(step)
    
    # Auswertung des stabilen eingeschwungenen Bereichs (letzte 60%)
    start_idx = int(len(t) * 0.4)
    t_stable = t[start_idx:]
    vd1_stable = vd1[start_idx:]

    # Interpolation auf gleichmäßiges Zeitraster für saubere FFT
    n = len(t_stable)
    t_uniform = np.linspace(t_stable[0], t_stable[-1], n)
    dt = t_uniform[1] - t_uniform[0] 
    vd1_uniform = np.interp(t_uniform, t_stable, vd1_stable)

    # FFT berechnen
    amp_vd1 = np.abs(np.fft.rfft(vd1_uniform)) * 2 / n
    freq = np.fft.rfftfreq(n, d=dt)

    # --- STEUERSPANNUNG AUSLESEN ---
    # Reale Spannung V(vstr) aus der Simulation für diesen Step auslesen
    vdstr_wave = Vdstr.get_wave(step)
    v_ctrl = np.mean(vdstr_wave) 
    
    v_ctrl_list.append(v_ctrl)

    # Peak-Frequenz im gesamten Spektrum suchen (DC bei 0Hz ausgeblendet)
    valid_range = np.where(freq > 100e3)[0]
    if len(valid_range) > 0:
        peak_idx = valid_range[np.argmax(amp_vd1[valid_range])]
        f_peak = freq[peak_idx]
    else:
        f_peak = 0
    f_peak_list.append(f_peak)

f_peak_mhz = np.array(f_peak_list) / 1e6
v_ctrl_np = np.array(v_ctrl_list)

# Berechnungen für das Diagramm-Label
f_min = min(f_peak_mhz)
f_max = max(f_peak_mhz)
diff_f = f_max - f_min

# Mittenfrequenz über den mittleren Index ermitteln
idx_mitte = len(f_peak_mhz) // 2
f_mitte = f_peak_mhz[idx_mitte]
v_mitte = v_ctrl_np[idx_mitte]

# --------------------------------------------------------------------------------------------------------------------------------
# ÄNDERUNG: Jetzt im sauberen 3er-Layout (3, 1, 3)
plt.subplot(3, 1, 3)
plt.plot(v_ctrl_np, f_peak_mhz, 'o-', color='green',
         label=f"VCO Kennlinie (Ist)\nMitte ({v_mitte:.2f} V) = {f_mitte:.2f} MHz\nMin = {f_min:.2f} MHz\nMax = {f_max:.2f} MHz\nHub = {diff_f:.2f} MHz")

# plt.plot([1.77, 6.45], [5.0, 6.0], linestyle="-", color="red", label="Soll-Kennlinie (Ideal)")

plt.xlabel(r"Steuerspannung $V_{str}$ in V")
plt.ylabel("Frequenz in MHz")

# Flexibles X-Limit basierend auf deinen realen Vstr-Werten
plt.xlim(v_ctrl_np.min() * 0.95, v_ctrl_np.max() * 1.05)
# plt.ylim(4.8, 6.2)

plt.axhline(5, color="red", linestyle="--", label=r"Untere Frequenz 5.0 MHz")
plt.axhline(5.5, color="red", linestyle="--", label=r"Mittenfrequenz 5.5 MHz")
plt.axhline(6, color="red", linestyle="--", label=r"Obere Frequenz 6.0 MHz")

plt.grid(True, which="both", linestyle="--")
plt.legend(loc="upper left")

plt.tight_layout() # Verhindert, dass sich Achsenbeschriftungen überlappen
plt.show()