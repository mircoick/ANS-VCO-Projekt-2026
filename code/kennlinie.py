import numpy as np
import pandas as pd
import scipy.signal as sig
import matplotlib.pyplot as plt
import glob
import os

list = np.array([0,1,2,3,4,5,6,7,8,9,10])
peaks = np.array([])

def datas(data,type):
    data = data.drop([0, 1])

    data[type] = data[type].str.replace("," , ".")
    data["Channel A"] = data["Channel A"].str.replace("," , ".")

    data["Channel A"] = data["Channel A"].astype(float)
    data[type] = data[type].astype(float)
    return data



for i in list:

    plt.subplot(3, 2, (1,2))

    list_of_filest = glob.glob(f'data/kennlinie/20260710_t_{i}/*')
    latest_filet = max(list_of_filest, key=os.path.getctime)

    data_t = pd.read_csv(latest_filet, sep=';')
    data_t = datas(data_t,"Time")

    plt.plot(data_t["Time"],data_t["Channel A"],label = f"{i*100} mV")

    plt.subplot(3, 2, (3,5))
    list_of_files = glob.glob(f'data/kennlinie/20260710_fft_{i}/*')
    latest_file = max(list_of_files, key=os.path.getctime)

    data_fft = pd.read_csv(latest_file, sep=';')
    data_fft = datas(data_fft,"Frequency")

    plt.plot(data_fft["Frequency"],data_fft["Channel A"],label = f"{i*100} mV")

    ind = data_fft["Channel A"].idxmax()
    freq = data_fft["Frequency"][ind]
    peaks = np.append(peaks,freq)



print(peaks)

plt.xlim(4.8,6.2)
plt.grid()
plt.xlabel("Frequenz in MHz")

plt.axvline(5.5, color="red", linestyle="--", label=r"Mittenfrequenz 5.5 MHz")
plt.axvline(5.0, color="red", linestyle="--", label=r"Untere Grenzfrequenz 5.0 MHz")
plt.axvline(6.0, color="red", linestyle="--", label=r"Obere Grenzfrequenz 6.0 MHz")

#plt.legend()

plt.subplot(3, 2, (4,6))
plt.plot(list*100,peaks, "o-")
plt.xlabel("U in mV")
plt.ylabel("Frequenz in MHz")

plt.axhline(5, color="red", linestyle="--", label=r"Untere Frequenz 5.0 MHz")
plt.axhline(5.5, color="red", linestyle="--", label=r"Mittenfrequenz 5.5 MHz")
plt.axhline(6, color="red", linestyle="--", label=r"Obere Frequenz 6.0 MHz")
plt.grid()

plt.show()
