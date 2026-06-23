import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 1. Set up the figure and axis
fig, ax = plt.subplots(figsize=(8, 4))      
ax.set_title("sync_three (Travelling Wave) Animation")
ax.set_xlabel("Distance (in degrees)")
ax.set_ylabel("Amplitude")

# Set x-axis ticks at intervals of 60 and turn on the grid
ax.set_xticks(np.arange(0, 361, 60))
ax.set_yticks(np.arange(-2, 2.5, 0.5))
ax.grid(True)

# Added 'label' to distinguish
line1, = ax.plot([], [], lw=1, color='red')
line2, = ax.plot([], [], lw=1, color='green')
line3, = ax.plot([], [], lw=1, color='blue')
line4, = ax.plot([], [], lw=1, color='cyan', label='Total Sum')

# Display a legend in the top right corner
ax.legend(loc="upper right")

# 2. Define the x data (distance)
x = np.linspace(0, 360, 720)

# 3. Initialization function
def init():
    line1.set_data([], [])
    line2.set_data([], [])
    line3.set_data([], [])
    line4.set_data([], [])
    return line1, line2, line3, line4

# 4. Animation function
def animate(t):
    y1 = np.sin(x * (np.pi / 180)) * np.sin(0.008 * np.pi * t)
    y2 = np.sin((x - 120) * (np.pi / 180)) * np.sin(0.008 * np.pi * t - (2 * np.pi/3))
    y3 = np.sin((x - 240) * (np.pi / 180)) * np.sin(0.008 * np.pi * t - (4 * np.pi/3))
    y4 = y1 + y2 + y3

    # Update data for all four lines
    line1.set_data(x, y1)
    line2.set_data(x, y2)
    line3.set_data(x, y3)
    line4.set_data(x, y4)

    # Return all four lines so Matplotlib knows to redraw them
    return line1, line2, line3, line4

# 5. Create the animation object
ani = animation.FuncAnimation(
    fig, animate, init_func=init, frames=250, interval=20, blit=True
)

# 6. Generate the GIF and display the animation
print("Generating GIF, please wait...") # Added a print statement because saving takes a few seconds
ani.save("sync_three.gif", writer="pillow", fps=50)
print("GIF saved successfully!")
plt.show()