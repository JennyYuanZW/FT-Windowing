import numpy as np
import matplotlib.pyplot as plt

# Generate some data
x = np.arange(0, 10, 0.1)
y = np.sin(x)

# Create a plot with grid lines spaced out each unit
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('My plot')
plt.grid(which='major', axis='both', linestyle='--', linewidth=0.5, color='gray')
plt.grid(which='minor', axis='both', linestyle=':', linewidth=0.5, color='black')
plt.xticks(np.arange(0, 10.5, 1))
plt.yticks(np.arange(-1, 1.5, 0.5))
plt.show()