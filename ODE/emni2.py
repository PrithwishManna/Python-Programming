import numpy as np
import matplotlib.pyplot as plt

# 1. Define the grid of points (x, y)
x = np.linspace(-5, 5, 20)
y = np.linspace(-5, 5, 20)
X, Y = np.meshgrid(x, y)

# 2. Define the system of equations: 
# x' = 5x + 4y
# y' = x + 2y
U = 5*X + 4*Y
V = 1*X + 2*Y

# 3. Normalize the arrows (makes them all the same length)
# This prevents long arrows from cluttering the graph
length = np.sqrt(U**2 + V**2)
# Avoid division by zero at the origin
length[length == 0] = 1 
U /= length
V /= length

# 4. Create the plot
plt.figure(figsize=(8, 8))

# Use 'quiver' to draw the arrows
plt.quiver(X, Y, U, V, color='cornflowerblue', pivot='mid', alpha=0.8)

# 5. Add the "Base Lines" (The Eigenvectors)
# Line 1 (Fast): y = 0.25x
# Line 2 (Slow): y = -x
x_line = np.linspace(-5, 5, 100)
plt.plot(x_line, 0.25*x_line, 'r--', label='Fast Line (y=0.25x)', linewidth=2)
plt.plot(x_line, -1*x_line, 'g--', label='Slow Line (y=-x)', linewidth=2)

# Formatting
plt.axhline(0, color='black', lw=1)
plt.axvline(0, color='black', lw=1)
plt.xlim([-5, 5])
plt.ylim([-5, 5])
plt.xlabel('x')
plt.ylabel('y')
plt.title("Direction Field for x' = 5x+4y, y' = x+2y")
plt.legend(loc='upper left')
plt.grid(alpha=0.3)

plt.show()