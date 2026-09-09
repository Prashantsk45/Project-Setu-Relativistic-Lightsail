================================================================================
PROJECT SETU: FUNDAMENTAL PHYSICS & MATHEMATICAL DERIVATIONS
Author: Prashant S. Kamble
================================================================================

1. CLASSICAL & QUANTUM DERIVATION OF PHOTON RADIATION THRUST
--------------------------------------------------------------------------------
1.1 From Maxwell's Stress Tensor:
The electromagnetic momentum flux across a surface S with outward normal n
is governed by the volume integral of the Lorentz force density:

  F = integral_S [T . n] dA - epsilon_0 * mu_0 * d/dt [integral_V S_vec dV]

where T is the Maxwell Stress Tensor:
  T_ij = epsilon_0 * (E_i * E_j - 0.5 * delta_ij * E^2) 
         + (1/mu_0) * (B_i * B_j - 0.5 * delta_ij * B^2)

For a monochromatic plane wave at normal incidence, the radiation pressure is:
  P_rad = <T_zz> = (1 + R) * <S> / c = (1 + R) * I / c

Multiplying by sail surface area A (where P_laser = I * A):
  F = [(1 + R) * P_laser] / c


2. RELATIVISTIC DOPPLER REDSHIFT ON ACCELERATING REFLECTORS
--------------------------------------------------------------------------------
When a reflector recedes at speed v = beta * c, the frequency transformation
from source frame S to spacecraft moving frame S' is:

  nu' = nu_0 * sqrt[(1 - beta) / (1 + beta)]

Upon reflection, the re-emitted wave undergoes a second Doppler transformation
back to the emitter/observer frame:

  nu'' = nu' * sqrt[(1 - beta) / (1 + beta)] = nu_0 * [(1 - beta) / (1 + beta)]

Because photon energy is E = h * nu, the received laser power P_rec scales as:

  P_rec(beta) = P_src * [(1 - beta) / (1 + beta)]


3. RELATIVISTIC EQUATION OF MOTION (LORENTZ ACCELERATION)
--------------------------------------------------------------------------------
In the laboratory (Earth) observer inertial frame, relativistic momentum is:

  p = gamma * m * v = (m * v) / sqrt(1 - beta^2)

The applied net photon force is:
  F = dp/dt = d/dt (gamma * m * v) = gamma^3 * m * (dv/dt) = gamma^3 * m * a

Therefore, the instantaneous coordinate acceleration is:
  a(beta) = F / (gamma^3 * m)
  a(beta) = [2 * P_src / (m * c * gamma^3)] * [(1 - beta) / (1 + beta)]
  a(beta) = [2 * P_src / (m * c)] * (1 - beta)^2 * sqrt(1 - beta^2)


4. STEFAN-BOLTZMANN DUAL-SIDED VACUUM RADIATIVE EQUILIBRIUM
--------------------------------------------------------------------------------
A thin planar membrane in deep-space vacuum achieves thermal equilibrium
when absorbed laser optical power equals total dual-sided radiative emission:

  Q_in = Q_out
  alpha * P_laser = (A_front + A_back) * epsilon * sigma * (T_eq^4 - T_space^4)

Since A_front = A_back = A_sail and T_space = 2.725 K << T_eq:
  alpha * P_laser = 2 * epsilon * sigma * A_sail * T_eq^4

Solving for the equilibrium core temperature T_eq:
  T_eq = [ ((1 - R) * P_laser) / (2 * epsilon * sigma * A_sail) ]^(1/4)
================================================================================
