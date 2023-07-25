import matplotlib.pyplot as plt

# Data for the four games
games = ['Jump', 'Game Flow', 'Difficulty']
BnR_values = [4.45, 4, 3.09]
SM64_values = [3.16, 3.08, 4.16]
DK64_values = [3.5, 3.5, 3.25]
BK_values = [4.42, 4.42, 2.71]

# Set the width of the bars
bar_width = 0.15

# Positions for the bars on the x-axis
x_positions = range(len(games))

# Create the bar chart for BnR game values
plt.bar(x_positions, BnR_values, width=bar_width, label='BnR', alpha=0.8, edgecolor='black')

# Create the bar chart for SM64 game values (shifted by bar_width)
plt.bar([pos + bar_width for pos in x_positions], SM64_values, width=bar_width, label='SM64', alpha=0.8, edgecolor='black')

# Create the bar chart for DK64 game values (shifted by 2 * bar_width)
plt.bar([pos + 2 * bar_width for pos in x_positions], DK64_values, width=bar_width, label='DK64', alpha=0.8, edgecolor='black')

# Create the bar chart for BK game values (shifted by 3 * bar_width)
plt.bar([pos + 3 * bar_width for pos in x_positions], BK_values, width=bar_width, label='BK', alpha=0.8, edgecolor='black')

# Set the x-axis tick positions and labels
plt.xticks([pos + 1.5 * bar_width for pos in x_positions], games, fontsize=12)

# Add labels and title
plt.xlabel('Categories', fontsize=14)
plt.ylabel('Values', fontsize=14)
plt.title('Game Ratings - Jump, Game Flow, Difficulty', fontsize=16)
plt.legend()

# Customize the appearance of the plot
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.ylim(0, 5)
plt.tight_layout()

# Save the plot as a PNG image
plt.savefig('game_ratings.png', dpi=300)

# Show the chart
plt.show()
