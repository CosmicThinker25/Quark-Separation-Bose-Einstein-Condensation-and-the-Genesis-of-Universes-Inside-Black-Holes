import numpy as np
import matplotlib.pyplot as plt

# Fig B1 — Tolman perturbative shifts vs R/ξ
R_over_xi = np.array([10, 15, 20, 30, 40, 60])
shift_percent = 5*(1/R_over_xi) + 1  # synthetic ~1–5% decreasing

plt.figure()
plt.plot(R_over_xi, shift_percent, marker="o")
plt.xlabel(r"$R/\xi$")
plt.ylabel("Shift in peak Δt/H (%)")
plt.title("Fig. B1 — Tolman perturbative shifts vs curvature scale")
plt.grid(True, linestyle=":")
plt.savefig("Fig_B1.png", dpi=200, bbox_inches="tight")
plt.close()
