#Salpeter IMF, alpha is 2.35

import numpy as np
import matplotlib.pyplot as plt

def salpeter_imf(mass, alpha=2.35, constant=1.0):
    """Salpeter IMF: xi(m) = constant * m^(-alpha)"""
    
    return constant * mass**(-alpha)

m_min = 0.1
m_max = 100
mass = np.logspace(np.log10(m_min), np.log10(m_max),1000)

def normalize_imf(mass, imf_values):
    integral = np.trapz(imf_values, mass)
    return imf_values / integral

alpha = 2.35
xi = salpeter_imf(mass, alpha=alpha)
xi_normalized = normalize_imf(mass, xi)

plt.figure(figsize=(8,6))
plt.loglog(mass, xi_normalized, label="Salpeter IMF (a={alpha})")
plt.xlabel("Mass")
plt.ylabel("IMF")
plt.title("Salpeter Initial mass function")
plt.grid(True, which="both", ls="--")
plt.legend()
plt.show()
