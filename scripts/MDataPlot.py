import matplotlib.pyplot as plt

# Generate your data points
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [1, 8, 27, 64, 125]
y3 = [1, 16, 81, 256, 625]

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the data points
ax.plot(x, y1, label='Data 1')
ax.plot(x, y2, label='Data 2')
ax.plot(x, y3, label='Data 3')

# Add legend
ax.legend()

# Set labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Multiple Data Points')

# Display the plots
plt.show()
