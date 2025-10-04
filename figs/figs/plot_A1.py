import numpy as np
import matplotlib.pyplot as plt

# Fig A1 — dual softening (baseline vs bag+gap proxy)
x = np.linspace(-2, 2, 300)
baseline = 0.25 + 0.05*np.tanh(1.5*x)
bag_gap = 0.22 + 0.06*np.tanh(1.2*x)
band = 0.10 * baseline  # ±10% band

plt.figure()
plt.plot(x, baseline, label="Baseline")
plt.plot(x, bag_gap, linestyle="--", label="Bag+Gap proxy")
plt.fill_between(x, bag_gap - band, bag_gap + band, alpha=0.2, label="±10% priors band")
plt.xlabel("Density scale (arb.)")
plt.ylabel(r"$c_s^2$ (effective)")
plt.title("Fig. A1 — Dual softening: baseline vs bag+gap (±10% band)")
plt.legend()
plt.savefig("Fig_A1.png", dpi=200, bbox_inches="tight")
plt.close()
