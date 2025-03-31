import numpy as np
import matplotlib.pyplot as plt

# Constants
Ka = 2e-5  # Acetic acid dissociation constant
Kb = 2e-5  # Ammonia base constant
pKa = -np.log10(Ka)
pKb = -np.log10(Kb)
C_acid = 1  # Molarity of CH3COOH
C_base = 1  # Molarity of NH3
V_acid = 25  # Initial volume of CH3COOH in cm³

# Volume of NH3 added (0 to 50 cm³ in 0.01 cm³ steps)
V_base = np.arange(0, 50.01, 0.01)
pH_values = []

for Vb in V_base:
    if Vb == 0:
        H_conc = np.sqrt(Ka * C_acid)
        pH = -np.log10(H_conc)
    elif Vb < V_acid:
        A_minus = (C_base * Vb) / (V_acid + Vb)
        HA = (C_acid * V_acid - C_base * Vb) / (V_acid + Vb)
        pH = pKa + np.log10(A_minus / HA)
    elif Vb == V_acid:
        A_minus_conc = C_acid * V_acid / (V_acid + Vb)
        OH_conc = np.sqrt(Kb * A_minus_conc)
        pOH = -np.log10(OH_conc)
        pH = 14 - pOH
    else:
        excess_NH3 = (C_base * (Vb - V_acid)) / (V_acid + Vb)
        pOH = pKb - np.log10(excess_NH3)
        pH = 14 - pOH

    pH_values.append(pH)

# Plot
plt.figure(figsize=(8, 5))
plt.plot(V_base, pH_values, label="Titration Curve", color="b")
plt.axvline(25, linestyle="--", color="r", label="Equivalence Point")
plt.xlabel("Volume of NH3 Added (cm³)")
plt.ylabel("pH")
plt.title("Titration of 1M CH3COOH with 1M NH3")
plt.legend()
plt.grid()
plt.show()
