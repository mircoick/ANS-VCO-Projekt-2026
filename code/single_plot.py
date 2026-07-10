import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sample = "04"

data_t = pd.read_csv(f"data/20260709/20260709_{sample}.csv", sep=';')
data_fft = pd.read_csv(f"data/kennlinie/20260709_fft/20260709_fft_{sample}.csv", sep=';')

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
plt.plot(data_fft["Frequency"], data_fft["Channel A"])
plt.plot(freq,max,"o")
plt.xlabel(r"Frequenz in f")
plt.ylabel("Channel A")
plt.grid()

plt.show()