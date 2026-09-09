"""
Project Setu: Relativistic Kinematics & Coordinate Trajectory Integration
Author: Prashant S. Kamble

Models 1D coordinate acceleration of a 4.0 m beamed lightsail driven by a
100 GW laser array, accounting for relativistic Doppler shift and Lorentz factor.
"""

import numpy as np
import matplotlib.pyplot as plt

# Physical constants and mission parameters
c = 299792458.0           # Speed of light (m/s)
P_laser = 100.0e9         # Laser array power: 100 GW
R_opt = 0.997821          # FDTD metasurface reflectance (99.78%)
m_spacecraft = 0.002      # Total launch mass: 2.0 g (payload + sail)
t_burn = 180.0            # Propulsion burn duration: 180 s

# Initial radiation force and acceleration at t = 0
F0 = ((1.0 + R_opt) * P_laser) / c  # Initial thrust (666.40 N)
a0 = F0 / m_spacecraft              # Initial coordinate acceleration (333,200 m/s^2)

# Relativistic trajectory time-stepping
dt = 0.1
t_array = np.arange(0, t_burn + dt, dt)
v_array = np.zeros_like(t_array)
a_array = np.zeros_like(t_array)
z_array = np.zeros_like(t_array)

v_curr = 0.0
z_curr = 0.0

for idx, t in enumerate(t_array):
    beta = v_curr / c
    # Relativistic Doppler thrust reduction: F(v) = F0 * (1 - beta) / (1 + beta)
    F_inst = F0 * ((1.0 - beta) / (1.0 + beta))
    # Relativistic coordinate acceleration: dv/dt = (F / m) * (1 - beta^2)^(3/2)
    gamma_factor = (1.0 - beta**2)**1.5
    a_inst = (F_inst / m_spacecraft) * gamma_factor
    
    a_array[idx] = a_inst
    v_array[idx] = v_curr
    z_array[idx] = z_curr
    
    v_curr += a_inst * dt
    z_curr += v_curr * dt

# Final trajectory metrics
v_final_kms = v_array[-1] / 1000.0
beta_final = v_array[-1] / c
z_final_million_km = z_array[-1] / 1.0e9

print("=" * 65)
print("       PROJECT SETU: RELATIVISTIC TRAJECTORY TELEMETRY")
print("=" * 65)
print(f"Laser Emitter Power         : {P_laser/1e9:.1f} GW")
print(f"Spacecraft Launch Mass      : {m_spacecraft*1000:.1f} grams")
print(f"Initial Photon Force (F0)   : {F0:.2f} N")
print(f"Initial Acceleration (a0)   : {a0/9.80665:,.1f} G ({a0:,.1f} m/s^2)")
print(f"Propulsion Burn Time        : {t_burn:.1f} seconds (3.0 minutes)")
print(f"Final Velocity Reached      : {v_final_kms:,.1f} km/s")
print(f"Relativistic Speed Ratio    : {beta_final:.4f} c ({beta_final*100:.2f}% speed of light)")
print(f"Laser Acceleration Distance : {z_final_million_km:,.2f} Million Kilometers")
print(f"Transit Time to Alpha Cent. : {4.2465 / beta_final:.2f} Years")
print("=" * 65)

# Milestone timeline summary
print("\n--- RELATIVISTIC FLIGHT PROGRESS TIMELINE ---")
print(f"{'Time (s)':<10} | {'Velocity (km/s)':<18} | {'Fraction (v/c)':<18} | {'Distance (M km)':<15}")
print("-" * 70)
for t_mark in [0, 30, 60, 90, 120, 150, 180]:
    idx_mark = int(t_mark / dt)
    print(f"{t_array[idx_mark]:<10.0f} | {v_array[idx_mark]/1000.0:<18,.1f} | {v_array[idx_mark]/c:<18.4f} | {z_array[idx_mark]/1e9:<15.2f}")
print("-" * 70)

# Trajectory plot
plt.figure("Project Setu: Relativistic Trajectory Line Curve", figsize=(10, 6))
plt.plot(t_array, v_array / 1000.0, color='#00aaff', linewidth=3.0, label=r'Spacecraft Velocity $v(t)$ (Relativistic Engine)')
plt.axhline(y=c * 0.20 / 1000.0, color='#ff2255', linestyle='--', linewidth=2.0, label=r'Target Velocity $0.20c$ ($60,000\text{ km/s}$)')
plt.title("Project Setu: 180-Second Relativistic Velocity Trajectory (0 to 0.20c)", fontsize=14, fontweight='bold', pad=14)
plt.xlabel("Propulsion Laser Burn Time (Seconds)", fontsize=12, fontweight='bold')
plt.ylabel("Spacecraft Velocity (km/s)", fontsize=12, fontweight='bold')
plt.xlim(0, 180)
plt.ylim(0, 65000)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=11, loc='upper left')
plt.tight_layout()

plt.savefig("D:/CFD/Project Setu/figures/Figure_1_Relativistic_Velocity_Profile.png", dpi=300)
print("\n[SUCCESS] Trajectory curve saved to D:/CFD/Project Setu/figures/Figure_1_Relativistic_Velocity_Profile.png")

# Display plot
plt.show()