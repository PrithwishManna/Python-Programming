import numpy as np
import matplotlib.pyplot as plt

# Define the time range
t = np.linspace(0, 2, 500)

# Define the displacement equation
x = (np.sqrt(5) / 4) * np.exp(-4 * t) * np.cos(8 * t - 0.4636)

# Define the upper and lower damping envelopes
envelope_upper = (np.sqrt(5) / 4) * np.exp(-4 * t)
envelope_lower = -(np.sqrt(5) / 4) * np.exp(-4 * t)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(t, x, 'b-', label='Displacement x(t)', linewidth=2)
plt.plot(t, envelope_upper, 'r--', label='Damping Envelope')
plt.plot(t, envelope_lower, 'r--')

# Formatting the graph
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.title('Free, Damped Motion of the Spring-Mass System')
plt.xlabel('Time (t) in seconds')
plt.ylabel('Displacement (x) in feet')
plt.xlim(-0.1, 1.5)
plt.grid(True, linestyle=':', alpha=0.7)
plt.legend()

# Display the graph
plt.show()




