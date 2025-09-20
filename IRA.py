#Instantaneous Recyclling Approximation
import numpy as np
import matplotlib.pyplot as plt

t_max = 30.0
dt = 0.1
n_steps = int(t_max / dt)
M_gas_init = 1e10
Z_init = 0.001
SFR_coeff = 1e-2
yield_metal = 0.02
R = 0.3

time = np.arange(0,t_max, dt)
M_gas = np.zeros(n_steps)
Z = np.zeros(n_steps)
M_star = np.zeros(n_steps)

M_gas[0] = M_gas_init
Z[0] = Z_init
M_star[0] = 0.0

for i in range(1, n_steps):
    SFR = SFR_coeff * M_gas[i-1]
    dM_gas = -SFR * dt + R * SFR * dt
    M_star[i] = M_star[i-1] + (1 - R) * SFR * dt
    M_gas[i] = M_gas[i-1] + dM_gas
    
    dZ = (yield_metal * R * SFR * dt - Z[i-1] * SFR * dt) / M_gas[i-1]
    Z[i] = Z[i-1] + dZ
    
    if M_gas[i] < 0:
        M_gas[i] = 0
        Z[i] = Z[i-1]
        
plt.figure(figsize=(10,6))
plt.subplot(2,1,1)
plt.plot(time, M_gas / M_gas_init, label="Gas Mass (Normalized)")
plt.plot(time, M_star / M_gas_init, label="Stellar Mass (Normalized)")
plt.xlabel("TIme(Gry)")
plt.ylabel("Metallicity")
plt.legend()

plt.tight_layout()
plt.show()
