import numpy as np
import matplotlib.pyplot as plt

# 1. Define the Energy/Momentum Scale (k) - Rewinding to Big Bang
# k = 1 is today, k -> 10^19 is the Planck scale (t -> 0)
k = np.logspace(0, 19, 500)

# 2. Level 2: Asymptotic Safety (Running of G)
# G(k) ~ g* / k^2. (Relative to G_today = 1)
# As k -> infinity, G -> 0
G_running = 1 / k**2 

# 3. Level 2: Non-Commutative Geometry (Minimum Volume)
# In classical physics, V ~ k^-3 (shrinks to 0 as k -> inf)
V_classical = 1 / k**3
# In NCG, V hits a floor at the Planck scale (V_min ~ 1, relative units here)
V_NCG = np.maximum(V_classical, 1e-5) # Saturates at Planck volume

# 4. Level 3: Information Density (rho_Phi)
# rho = Information / Volume.
# If Volume hits a floor (NCG), and Information is bounded, rho hits a ceiling.
rho_classical = k**4 # Classical radiation blowup
rho_NCG_capped = np.minimum(rho_classical, 1e5) # Capped by Holographic/NCG bound

# Plotting
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# --- Plot 1: The Fading of Gravity (ASG) ---
ax1.loglog(k, G_running, 'b-', linewidth=3, label="Running $G(k) \\propto 1/k^2$")
ax1.axvline(1e19, color='red', linestyle='--', label="Planck Scale ($k_{Pl}$)")
ax1.set_title("Level 2: Asymptotic Safety\nGravity 'Turns Off' at Origin", fontsize=12)
ax1.set_xlabel("Energy Scale ($k$) $\\to$ Big Bang")
ax1.set_ylabel("Relative Gravitational Strength $G(k)$")
ax1.legend()
ax1.grid(True, which="both", ls="--", alpha=0.5)

# --- Plot 2: The Pixelation of Space (NCG) ---
ax2.loglog(k, V_classical, 'k--', label="Classical Volume ($\\propto 1/k^3$)")
ax2.loglog(k, V_NCG, 'g-', linewidth=3, label="NCG Volume ($V_{min}$ floor)")
ax2.axvline(1e19, color='red', linestyle='--', label="Planck Scale ($k_{Pl}$)")
ax2.set_title("Level 2: Non-Commutative Geometry\nSpace 'Pixelates' at Origin", fontsize=12)
ax2.set_xlabel("Energy Scale ($k$) $\\to$ Big Bang")
ax2.set_ylabel("Spatial Volume")
ax2.legend()
ax2.grid(True, which="both", ls="--", alpha=0.5)

plt.suptitle("The Quantum Hardware: How Level 2 Prevents the Infinite Singularity", fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()