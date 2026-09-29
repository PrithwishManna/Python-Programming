import numpy as np
import matplotlib.pyplot as plt

# Define the Hamiltonian function
def H(x, y):
    return 0.5*y**2 + 0.5*x**2 - (1/24)*x**4

# Define the system of ODEs for the vector field
def system(x, y):
    dx = y
    dy = -x + (x**3)/6
    return dx, dy

# Create a grid of points
x = np.linspace(-5, 5, 400)
y = np.linspace(-4, 4, 400)
X, Y = np.meshgrid(x, y)
Z = H(X, Y)

plt.figure(figsize=(10, 8))

# Plot level curves (trajectories)
# We choose levels specifically to show the center and the separatrix
levels = [0.1, 0.5, 1.0, 1.5, 2.0]
cp = plt.contour(X, Y, Z, levels=levels, colors='blue')
plt.clabel(cp, inline=True, fontsize=8)

# Plot the vector field (direction arrows)
x_q = np.linspace(-5, 5, 20)
y_q = np.linspace(-4, 4, 20)
X_q, Y_q = np.meshgrid(x_q, y_q)
DX, DY = system(X_q, Y_q)

# Normalize arrows for better visibility
M = np.sqrt(DX**2 + DY**2)
M[M == 0] = 1 # Avoid division by zero
plt.quiver(X_q, Y_q, DX/M, DY/M, color='red', alpha=0.5, pivot='mid')

plt.title('Trajectories of the Dynamical System $H(x, y) = C$')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', lw=1)
plt.axvline(0, color='black', lw=1)
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()