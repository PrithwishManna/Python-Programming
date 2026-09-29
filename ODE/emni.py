import numpy as np
import matplotlib.pyplot as plt

# 1. Define the Nonlinear System
def system(x, y):
    dxdt = 2*x - x**2 - x*y
    dydt = 3*y - 2*y**2 - 3*x*y
    return dxdt, dydt

# 2. Manual Integrator (Euler Method) to find Basins
def get_destination(x0, y0, dt=0.1, steps=200):
    curr_x, curr_y = x0, y0
    for _ in range(steps):
        dxdt, dydt = system(curr_x, curr_y)
        curr_x += dxdt * dt
        curr_y += dydt * dt
        
        # Early exit if it hits a known sink
        if np.sqrt((curr_x - 2)**2 + (curr_y - 0)**2) < 0.1:
            return 1  # Sink (2,0)
        if np.sqrt((curr_x + 1)**2 + (curr_y - 3)**2) < 0.1:
            return 2  # Sink (-1,3)
            
    return 0 # Neutral/Did not converge

# 3. Setup Grid
res = 100
x_vals = np.linspace(-1.5, 3.5, res)
y_vals = np.linspace(-1, 4.5, res)
X, Y = np.meshgrid(x_vals, y_vals)
basin_grid = np.zeros((res, res))

# 4. Compute Basin Map
for i in range(res):
    for j in range(res):
        basin_grid[i, j] = get_destination(X[i, j], Y[i, j])

# 5. Plotting
plt.figure(figsize=(10, 8))

# Shading the Basins
# 1 is Green (Sink 2,0), 2 is Blue (Sink -1,3)
cmap = plt.matplotlib.colors.ListedColormap(['white', '#ccffcc', '#cce6ff'])
plt.pcolormesh(X, Y, basin_grid, cmap=cmap, shading='auto', alpha=0.8)

# Vector Field
U, V = system(X, Y)
plt.streamplot(X, Y, U, V, color='gray', linewidth=0.8, density=1.2)

# Critical Points
plt.scatter([2], [0], color='green', s=100, edgecolors='black', label='Stable Node (2,0)', zorder=5)
plt.scatter([-1], [3], color='blue', s=100, edgecolors='black', label='Stable Node (-1,3)', zorder=5)
plt.scatter([0], [1.5], color='orange', s=100, edgecolors='black', label='Saddle (0, 1.5)', zorder=5)
plt.scatter([0], [0], color='red', s=100, edgecolors='black', label='Unstable Node (0,0)', zorder=5)

plt.axhline(0, color='black', lw=1)
plt.axvline(0, color='black', lw=1)
plt.title("Phase Portrait & Basins of Attraction (Manual Euler Integration)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc='upper right')
plt.grid(alpha=0.2)
plt.show()