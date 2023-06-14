import matplotlib.pyplot as plt

# Generate your data points
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
labels = ['A', 'B', 'C', 'D', 'E']

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the data points
ax.plot(x, y, 'bo')

# Add labels to the data points
for i in range(len(x)):
    ax.text(x[i], y[i], labels[i], ha='center', va='bottom')

# Set labels and title
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Data Points with Labels')

# Display the plots
plt.show()