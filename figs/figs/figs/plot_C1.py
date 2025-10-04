import numpy as np
import matplotlib.pyplot as plt

# Fig C1 — Damping spread vs dissipation proxy C
C_vals = np.linspace(0.5, 2.0, 30)
damping = 10 + 10*(C_vals-0.5)/(2.0-0.5)  # 10% → 20%

plt.figure()
plt.plot(C_vals, damping)
plt.xlabel("C (order-unity dissipation proxy)")
plt.ylabel("Damping in $\dot{H}(0)$ (%)")
plt.title("Fig. C1 — Damping spread vs C (proxy, order unity)")
plt.grid(True, linestyle=":")
plt.savefig("Fig_C1.png", dpi=200, bbox_inches="tight")
plt.close()
