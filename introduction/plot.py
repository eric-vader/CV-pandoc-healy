import matplotlib.pyplot as plt
import numpy as np
import math

# Define the range for n
n_values = np.arange(0, 11, 1)

# Define the functions
f_values = [(math.factorial(n+2)/2) for n in n_values]
g_values = [3**n for n in n_values]

# Plot the functions
plt.plot(n_values, f_values, label=r'$\frac{(n+2)!}{2}$', marker='o')
plt.plot(n_values, g_values, label=r'$3^n$', marker='o')

# Add title and legend
plt.title('Plot of (n+2)!/2 and 3^n')
plt.xlabel('n')
plt.legend()

# Display the plot
plt.grid(True)
plt.yscale('log')  # Set the y-axis to logarithmic scale for better visualization

# plt.savefig('plot.pdf', format='pdf', bbox_inches='tight')

plt.savefig('plot.pdf', format='pdf', bbox_inches='tight', transparent=True)
