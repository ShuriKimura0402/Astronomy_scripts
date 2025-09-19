#simple model of chemical evolution

import numpy as np
import matplotlib.pyplot as plt

M_tot = 1.0e10
Z_0 = 0.0
y = 0.02
psi_0 = 1.0e-10
t_max = 1.0e10
dt = 1.0e7
n_steps = int(t_max/dt)

time = np.zeros(n_steps)
M_gas = np.zeros(n_steps)
Z = np.zeros(n_steps)
M_gas[0] = M_tot
Z[0] = Z_0

for i in range(n_steps - 1):
    M_g = M_gas[i]
    Z_i = Z[i]
    
    psi = psi_0 * M_g
    dM_gas = -psi * dt
    dZ = (y * psi * dt) / M_g
    
    M_gas[i + 1] = M_g + dM_gas
    Z[i + 1] = Z_i + dZ
    time[i + 1] = time[i] + dt
    
    if M_gas[i + 1] < 0:
        M_gas[i + 1] = Z_0
        break

plt.figure(figsize=(10,6))

plt.subplot(2,1,1)
plt.plot(time / 1.0e9, M_gas / M_tot, label="Gass Mass (Normalized)")
plt.xlabel("Time(Gry)")
plt.ylabel("M_gas / M_tot")
plt.grid(True)
plt.legend()

plt.subplot(2,1,2)
plt.plot(time / 1.0e9, Z, label='Metallcity (Z)', color="orange")
plt.xlabel("Time (Gry)")
plt.ylabe("Metallicity(Z)")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
