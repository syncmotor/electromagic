import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 1. Set up the figure, the axis, and the plot element we want to animate
fig, ax = plt.subplots(figsize=(8, 4))
ax.set_title("sync_one (Standing Wave) Animation")
ax.set_xlabel("Distance (in degrees)")
ax.set_ylabel("Amplitude")
ax.set_xticks(np.arange(0, 361, 60))
ax.set_yticks(np.arange(-1.5, 2, 0.5))
ax.grid(True)

# Initialize an empty line object
line, = ax.plot([], [], lw=1, color='blue')

# 2. Define the x data (distance)
x = np.linspace(0, 360, 720)

# 3. Initialization function: plots the background of each frame
def init():
    line.set_data([], [])
    return (line,)

# 4. Animation function: this is called sequentially for each frame
def animate(t):
    # t is the frame number, functioning as time
    y = 1 * np.sin(x*(np.pi/180)) * np.sin(0.008 * np.pi * t)
    line.set_data(x, y)
    return (line,)

# 5. Create the animation object
# frames: number of frames, interval: delay between frames in milliseconds
ani = animation.FuncAnimation(
    fig, animate, init_func=init, frames=250, interval=20, blit=True
)

# 6. Generate the GIF and display the animation
print("Generating GIF, please wait...") # Added a print statement because saving takes a few seconds
ani.save("sync_one.gif", writer="pillow", fps=50)
print("GIF saved successfully!")
plt.show()