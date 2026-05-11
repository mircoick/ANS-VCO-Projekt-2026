from PyLTSpice import RawRead

from matplotlib import pyplot as plt

LTR = RawRead("kicad/VCO-Schwingkreis/NET_VCO-Schwingkreis.raw")

print(LTR.get_trace_names())
print(LTR.get_raw_property())

IR1 = LTR.get_trace("I(xq1:1)")
vd = LTR.get_trace("v(v-sweep)") 
steps = LTR.get_steps()
for step in range(len(steps)):
    print(steps[step])
    plt.plot(vd.get_wave(step), IR1.get_wave(step), label=steps[step])

plt.legend()  # order a legend
plt.grid()
plt.show()