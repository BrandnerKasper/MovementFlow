import matplotlib.pyplot as plt

# Create a figure and subplots
fig, axs = plt.subplots(2, 2, figsize=(8, 6))

# Generate your data for each subplot
x = [1, 2, 3, 4]
y1 = [1, 4, 9, 16]
y2 = [1, 8, 27, 64]
y3 = [1, 16, 81, 256]
y4 = [1, 32, 243, 1024]

# Plot the data on each subplot
axs[0, 0].plot(x, y1)
axs[0, 0].set_title('Plot 1')
axs[0, 1].plot(x, y2)
axs[0, 1].set_title('Plot 2')
axs[1, 0].plot(x, y3)
axs[1, 0].set_title('Plot 3')
axs[1, 1].plot(x, y4)
axs[1, 1].set_title('Plot 4')

# Adjust spacing between subplots
plt.tight_layout()

# Save the figure with all the subplots
plt.savefig('multiple_plots.png')

# Display the figure
plt.show()
