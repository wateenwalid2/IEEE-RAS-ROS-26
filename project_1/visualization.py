import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

plt.ion()
fig, ax = plt.subplots()

DRONE_COLORS = ['blue', 'green', 'purple', 'cyan', 'magenta', 'brown', 'orange', 'pink']

def draw(grid, drones, goals=None, no_fly_zones=None):
    ax.clear()

    if no_fly_zones:
        for (x, y) in no_fly_zones:
            ax.scatter(x, y, c='red', marker='X', s=100, zorder=3)

    legend_handles = []
    for i, d in enumerate(drones):
        color = DRONE_COLORS[i % len(DRONE_COLORS)]  # cycles if more drones than colors
        ax.scatter(d.position[0], d.position[1], c=color, s=80, zorder=3)
        ax.text(d.position[0] + 0.2, d.position[1] + 0.2, str(d.d_id), fontsize=8)
        legend_handles.append(mpatches.Patch(color=color, label=f'Drone {d.d_id} | {d.battery:.1f}%'))

    if goals:
        for (x, y) in goals:
            ax.scatter(x, y, c='orange', marker='X', s=100, zorder=3)

    ax.set_xlim(0, grid.grid_size)
    ax.set_ylim(0, grid.grid_size)
    ax.grid(True)
    ax.legend(handles=legend_handles, loc='upper left', fontsize=7)
    plt.pause(0.3)