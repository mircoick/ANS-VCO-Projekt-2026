import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

volts = "0"
sample = "01"

data_t = pd.read_csv(f"../data/20260710_t_{volts}/20260710_t_{volts}_{sample}.csv", sep=';')
data_fft = pd.read_csv(f"../data/20260710_fft_{volts}/20260710_fft_{volts}_{sample}.csv", sep=';')

def datas(data,type):
    data = data.drop([0, 1])

    data[type] = data[type].str.replace("," , ".")
    data["Channel A"] = data["Channel A"].str.replace("," , ".")

    data["Channel A"] = data["Channel A"].astype(float)
    data[type] = data[type].astype(float)
    return data


data_t = datas(data_t,"Time")
data_fft = datas(data_fft,"Frequency")

ind = data_fft["Channel A"].idxmax()

max = data_fft["Channel A"].max()
freq = data_fft["Frequency"][ind]
print(freq)
"""plt.subplot(2,1,1)
plt.plot(data_t["Time"], data_t["Channel A"])
plt.xlabel(r"Time in \mu s")
plt.ylabel("Channel A")
plt.grid()
plt.subplot(2,1,2)"""
plt.plot(data_fft["Frequency"], data_fft["Channel A"],label=fr"Messdaten bei $V_{{str}}={float(volts)*100:.2f}\,$mV")
plt.plot(freq,max,"o",label=f"Frequenzpeak bei {freq:.2f} MHz")
plt.xlabel(r"Frequenz in MHz")
plt.ylabel("Amplitude in dB")
plt.xlim(0,25)
plt.legend()
plt.grid()

plt.show()