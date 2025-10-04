# Siamese Universes v1.0 — Effective QGP → CFL/BEC → LQC Bounce with Guardrails

This repository contains the **official final version (v1.0)** of the manuscript:

📄 [Siamese_Universes_v1.0_Final.pdf](./Siamese_Universes_v1.0_FinalA.pdf)  
**Authors:** CosmicThinker & ChatGPT5  
**Date:** Oct 04, 2025  

---

## Abstract
We present a refined effective framework in which matter inside black holes undergoes a sequence of phases — quark–gluon plasma (QGP), color–flavor–locked (CFL) / Bose–Einstein condensation (BEC), and a loop quantum cosmology (LQC)–type bounce — culminating in nonsingular “Siamese” universes. The model includes explicit guardrails: mesoscopic validity (R ≫ ξ ~ 1/Δ), curved-GL perturbative treatment of σ(R), compact Israel–Darmois junctions, flat-prior parameter scans (≈10% bands), and a holographically guided dissipation proxy with C ∈ [0.5, 2]. Synthetic estimates include Tolman corrections O(1–5%) in Δt/H, ~3% reduction of σ at R/ξ=20, and ~15% damping in $\dot{H}(0)$ for C≈1.5, while preserving a robust bounce. A roadmap toward Einstein Toolkit (ETK) viscous GR-hydro simulations is outlined.

---

## Repository Contents
- **`Siamese_Universes_v1.0_Final.pdf`** — main paper (final version, Oct 2025).
- **`figs/`** — synthetic figures:
  - `Fig_A1.png`: Dual softening (baseline vs bag+gap proxy with ±10% prior band).  
  - `Fig_B1.png`: Tolman perturbative shifts (1–5%) in Δt/H vs curvature scale R/ξ.  
  - `Fig_C1.png`: Damping spread (~10–20%) vs dissipation proxy C.  
- *(Optional, upcoming)*: Python scripts to regenerate figures.

---

## Parameter Priors (summary)
| Parameter         | Symbol   | Range / Prior   | Notes                                   |
|-------------------|----------|-----------------|-----------------------------------------|
| Tolman factor     | δ_T      | 1–5%            | Perturbative shift in Δt/H              |
| Gap strength      | Δ        | lit.-guided     | Enters σ₀ ~ c_σ μ²Δ                     |
| Dissipation proxy | C        | [0.5, 2]        | Order unity (holography-inspired)       |
| Sound speed (CFL) | c_s²     | 0.15 ± 0.02     | Effective soft phase                    |

---

## Roadmap
- **Phase I**: Mesoscopic scans + RK45 toy evolution.  
- **Phase II**: Post-processing CLASS/ETK outputs with effective softening.  
- **Phase III**: Einstein Toolkit (2025 release) viscous GR-hydro, slow-rotation Kerr interiors.  

---

## Honest Statement
This is an **effective scoped toy model**. Proxies (Tolman, curved-GL O(λ), dissipation C) are used to quantify trends, **not** to claim ab initio microphysics near black hole horizons.  
All numerical values in the figures are **synthetic illustrations** only; they should be replaced by calibrated ETK outputs in future simulations.

---

## Citation
If you use or reference this work, please cite as: 
---

## License
This repository is released under the MIT License (see [LICENSE](./LICENSE) if present).

