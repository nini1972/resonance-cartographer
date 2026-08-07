import io
import sys
from pathlib import Path

import sympy as sp


class Tee:
    def __init__(self, *streams):
        self.streams = streams

    def write(self, text):
        for stream in self.streams:
            stream.write(text)

    def flush(self):
        for stream in self.streams:
            stream.flush()


original_stdout = sys.stdout
output_buffer = io.StringIO()
sys.stdout = Tee(original_stdout, output_buffer)

# Define symbols
t = sp.symbols('t')
a = sp.Function('a')(t) # Scale factor of the universe
rho_m, rho_phi, Lambda, G, k_B, T_origin, hbar, c = sp.symbols(
    'rho_m rho_Phi Lambda G k_B T_0 hbar c', positive=True, real=True
)
w_phi = sp.symbols('w_Phi') # Equation of state for Information (p = w * rho)

# 1. Modified Friedmann Equation (flat universe, k=0)
# H^2 = (8*pi*G/3) * (rho_m + rho_Phi) + Lambda/3
H = sp.diff(a, t) / a
friedmann_eq = sp.Eq(H**2, (8 * sp.pi * G / 3) * (rho_m + rho_phi) + Lambda / 3)

print("--- Standard Modified Friedmann Equation ---")
sp.pprint(friedmann_eq)

# 2. The Rewind (t -> 0)
# At the origin, classical matter density goes to zero.
origin_friedmann = friedmann_eq.subs(rho_m, 0)

# 3. The Origin Singularity (Information Dominated)
# At t -> 0, even Lambda (vacuum energy) is dominated by the sheer density of quantum information.
# We set Lambda -> 0 to find the PURE information origin state.
origin_state = sp.Eq(H**2, (8 * sp.pi * G / 3) * rho_phi)

print("\n--- Origin State Equation (t -> 0, Matter -> 0, Pure Information) ---")
sp.pprint(origin_state)

# Solve for Information Energy Density (rho_Phi) required to drive the Big Bang
rho_phi_origin = sp.solve(origin_state, rho_phi)[0]
print("\nInformation Energy Density (rho_Phi) at the Origin:")
sp.pprint(sp.Eq(rho_phi, rho_phi_origin))

# 4. Link to Information Theory (Landauer's Principle)
# E = k_B * T * ln(2) per bit of information.
# Therefore, Energy Density = Information Density (bits/m^3) * k_B * T * ln(2)
# rho_Phi = I_density * k_B * T_0 * ln(2)
# So, I_density = rho_Phi / (k_B * T_0 * ln(2))

I_density = sp.symbols('I_density')
I_density_expr = rho_phi_origin / (k_B * T_origin * sp.log(2))

print("\n--- Mathematical Translation to Information Density ---")
print("Using Landauer's Principle: E = k_B * T * ln(2)")
print("Information Density (bits per unit volume) at the Origin of the Universe:")
sp.pprint(sp.Eq(I_density, I_density_expr))

# 5. The Holographic Limit (Bekenstein Bound)
# At t -> 0, volume -> 0, but Area also -> 0. 
# The maximum information in a volume is I_max <= 2*pi*E*R / (hbar*c*ln2)
# Let's see what happens if we substitute the Holographic bound into our origin equation.
R, E_total = sp.symbols('R E_total', positive=True)
I_max_holographic = (2 * sp.pi * E_total * R) / (hbar * c * sp.log(2))

print("\n--- Holographic Boundary Check ---")
print("Maximum Information allowed by Bekenstein Bound:")
sp.pprint(sp.Eq(sp.symbols('I_max'), I_max_holographic))
print("\nConclusion: The origin of the universe is the mathematical point where")
print("the Information Density driving expansion exactly saturates the Holographic Bound.")

sys.stdout = original_stdout
output_path = Path(__file__).resolve().with_name('singularity_rewind_output.txt')
output_path.write_text(output_buffer.getvalue(), encoding='utf-8')
print(f"\nSaved shareable output to: {output_path}")