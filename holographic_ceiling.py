from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import numpy as np

# 1. Define the Time/Scale Rewind
# a = 1 is today, a -> 0 is the Big Bang
a = np.logspace(-4, 0, 500) # Scale factor
t_rewind = 1 / a # Simplified time rewind metric

# 2. Energy Densities (Relative units)
# Classical Matter: rho ~ a^-3 (Diverges to infinity at t->0)
rho_matter = a**(-3)

# Classical Radiation: rho ~ a^-4 (Diverges even faster to infinity at t->0)
rho_rad = a**(-4)

# Our Derived Information Density (rho_Phi)
# From our math: rho_Phi = 3H^2 / (8*pi*G)
# At early times, H^2 is dominated by the highest energy density.
# But because of the Holographic Bound, it saturates at the Planck limit.
rho_phi = np.minimum(rho_rad, 1e9) # Information density saturates at the Bekenstein ceiling

# The Holographic Ceiling (Bekenstein Bound limit at Planck scale)
holographic_ceiling = np.full_like(a, 1e9) 

# 3. Plotting the Simulator
fig = plt.figure(figsize=(16, 6))
gs = GridSpec(1, 3, figure=fig)

# --- Panel 1: The Macro Cosmic Web (a = 1) ---
ax1 = fig.add_subplot(gs[0, 0])
# Simulate a random cosmic web network
np.random.seed(42)
x, y = np.random.rand(50), np.random.rand(50)
ax1.scatter(x, y, s=np.random.randint(10, 200, 50), color='navy', alpha=0.6)
for i in range(50):
    for j in range(i+1, 50):
        if np.random.rand() > 0.95:
            ax1.plot([x[i], x[j]], [y[i], y[j]], 'k-', alpha=0.2)
ax1.set_title("Macro State: The Cosmic Web\n(Low $\\rho_\\Phi$, High Entropy)", fontsize=12)
ax1.set_xticks([])
ax1.set_yticks([])
ax1.set_facecolor('#f0f0f0')

# --- Panel 2: Gravitational Collapse (a = 0.1) ---
ax2 = fig.add_subplot(gs[0, 1])
# Simulate matter clumping
x2, y2 = np.random.normal(0.5, 0.15, 100), np.random.normal(0.5, 0.15, 100)
ax2.scatter(x2, y2, s=50, color='purple', alpha=0.7)
ax2.set_title("Collapse State: Structure Formation\n(Increasing $\\rho_\\Phi$, $T_{\\mu\\nu}^{\\Phi}$ active)", fontsize=12)
ax2.set_xticks([])
ax2.set_yticks([])
ax2.set_xlim(0, 1)
ax2.set_ylim(0, 1)
ax2.set_facecolor('#e6e6fa')

# --- Panel 3: The Information Singularity Rewind (Math Plot) ---
ax3 = fig.add_subplot(gs[0, 2])
ax3.loglog(a, rho_rad, 'r--', label='Classical Radiation ($a^{-4}$)', alpha=0.7)
ax3.loglog(a, rho_matter, 'b--', label='Classical Matter ($a^{-3}$)', alpha=0.7)
ax3.loglog(a, rho_phi, 'g-', linewidth=3, label='Information Density ($\\rho_\\Phi$)')
ax3.axhline(1e9, color='gold', linestyle='-', linewidth=2, label='Holographic Ceiling (Bekenstein)')

ax3.set_title("Genesis Rewind ($t \\to 0$)\nInformation Saturates Singularity", fontsize=12)
ax3.set_xlabel("Scale Factor ($a$) $\\to$ 0")
ax3.set_ylabel("Energy Density")
ax3.legend(fontsize=8, loc='upper left')
ax3.set_xlim(1e-4, 1)
ax3.set_ylim(1, 1e11)
ax3.grid(True, which="both", ls="--", alpha=0.5)

output_dir = Path(__file__).resolve().parent / 'assets' / 'images'
output_dir.mkdir(parents=True, exist_ok=True)
output_path = output_dir / 'holographic_ceiling.png'
plt.savefig(output_path, dpi=200, bbox_inches='tight')
plt.close()
print(f"Saved visualization to: {output_path}")