"""

"""


capacitance_rated = 25
voltage_rated = 2.5
power_rated = 8


import numpy as np
import matplotlib.pyplot as plt

u0 = np.linspace(voltage_rated/5.0, voltage_rated, num=101)
w0 = capacitance_rated*u0**2/2.0
w0rel = w0/w0.max()*100.0
t0 = w0/power_rated

plt.subplot(1,3,1)
plt.plot(u0, w0)
plt.grid(True)
plt.title("Energy vs Voltage")
plt.xlabel("Voltage [V]")
plt.ylabel("Energy [J]")
plt.axis([u0.min(), u0.max(), 0, w0.max()])

plt.subplot(1,3,2)
plt.plot(u0, w0rel)
plt.grid(True)
plt.title("Relative energy vs Voltage")
plt.xlabel("Voltage [V]")
plt.ylabel("Energy [%]")
plt.axis([u0.min(), u0.max(), 0, 100.0])

plt.subplot(1,3,3)
plt.plot(u0, t0)
plt.grid(True)
plt.title("Discharge time vs Voltage")
plt.xlabel("Voltage [V]")
plt.ylabel("Time [s]")
plt.axis([u0.min(), u0.max(), 0, t0.max()])



plt.show()


