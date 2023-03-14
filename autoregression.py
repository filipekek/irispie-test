import numpy as np

x = np.full((100), np.nan)
rho = 0.8
ss_x = 2
x[0] = -10

for t in range(1, 100):
    x[t] = rho * x[t-1] + (1 - rho) * ss_x
