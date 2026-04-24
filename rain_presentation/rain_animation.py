import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider
import numpy as np

x_min, x_max = -30, 30
y_min, y_max = 0, 30
mult_size = 3.0
speed = 0.5

def make_round(inp, lower, upper):
    diff = upper - lower
    if inp < lower:
        inp += diff
    if inp > upper:
        inp -= diff
    return inp

# Function to update the animation frame
def update(frame):
    global cube1, cube2, small_circles, v1, v2, v3_0, v3_1, v3_slider
    # Set the speeds of the cubes
    speed_mult = speed * speed_slider.val
    v1 = 0.0 * speed_mult
    v2 = -0.5 * speed_mult
    v3_0 = 0.0 * speed_mult
    v3_1 = -0.3 * speed_mult

    # Update cube positions based on their speeds
    v3 = v3_slider.val * speed_mult
    cube1.set_x(cube1.get_x() + v1 + v3)
    cube2.set_x(cube2.get_x() + v2 + v3)

    # Update small circle positions
    for circle in small_circles:
        x = circle.center[0] + v3_0 + v3
        y = circle.center[1] + v3_1
        x = make_round(x, x_min, x_max)
        y = make_round(y, y_min, y_max)
        circle.set_center((x, y))

    # Check if cubes have met, and if so, stop the animation
    if cube1.get_x() + 1 >= cube2.get_x():
        ani.event_source.stop()

    return [cube1] + [cube2] + small_circles

# Set up the figure and axes
fig, ax = plt.subplots()
ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)

# Create two cubes
cube1 = plt.Rectangle((x_min, 3 * mult_size), 3 * mult_size, 0.5 * mult_size, fc='b', label='cover')
cube2 = plt.Rectangle((x_max - mult_size, 0), 1 * mult_size, 2 * mult_size, fc='r', label='human')

# Add the cubes to the plot
ax.add_patch(cube1)
ax.add_patch(cube2)

# Create small circles all over the grid
grid_step = 2.0
small_circles = []
for x in np.arange(x_min, x_max, grid_step):
    for y in np.arange(y_min, y_max, grid_step):
        small_circles.append(plt.Circle((x, y), 0.1))

# Add small circles to the plot
for circle in small_circles:
    ax.add_patch(circle)

# Create the slider for v3
ax_v3 = plt.axes([0.25, 0.01, 0.65, 0.03], facecolor='lightgoldenrodyellow')
v3_slider = Slider(ax_v3, 'v3', 0.0, 1.0, valinit=0.0)

# Create the slider for speed
ax_speed = plt.axes([0.25, 0.06, 0.65, 0.03], facecolor='lightgoldenrodyellow')
speed_slider = Slider(ax_speed, 'speed', 0.1, 3.0, valinit=0.5)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=100, interval=10, blit=True, repeat=True)

# Show the plot
plt.show()
