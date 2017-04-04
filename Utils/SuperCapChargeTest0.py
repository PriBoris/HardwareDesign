"""
Simulating SuperCap charging with constant current via LTC3127

"""


import numpy as np
import matplotlib.pyplot as plt


u1 = 4.0
i1 = 1

u2_start = 0.0
u2_stop = 2.5

cap = 25


dt = 0.01
t_max = 100

t = np.arange(0, t_max, dt)
u2 = np.zeros(np.shape(t))

print("info: time array size = ", np.size(t))
print("info: u2 array size = ", np.size(u2))

n = np.size(t)

u2[0] = u2_start
for i in range(1, np.size(t)):
	u2_prev = u2[i-1]
	u2_next = u2_prev + dt*i1/cap

	if u2_next>u2_stop:
		u2_next = u2_stop

	u2[i] = u2_next



plt.plot(t, u2)
plt.grid(True)
plt.title("SuperCap voltage vs Time")
plt.xlabel("Time [s]")
plt.ylabel("Voltage [V]")
# plt.axis([t.min(), t_max, 0, t0.max()])
plt.show()




