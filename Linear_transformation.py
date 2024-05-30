import numpy as np
import matplotlib.pyplot as plt

cube_vertices = np.array([
    [0, 0, 0],
    [1, 0, 0],
    [1, 1, 0],
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 1],
    [1, 1, 1],
    [0, 1, 1]
])
def plot_cube(vertices, title):
    fig, axs = plt.subplots(1, 3, figsize=(18, 6))

    axs[0].scatter(vertices[:, 0], vertices[:, 1])
    for i in range(len(vertices)):
        for j in range(i + 1, len(vertices)):
            if np.sum(np.abs(vertices[i] - vertices[j]) == 1) == 1:
                axs[0].plot(*zip(vertices[i, :2], vertices[j, :2]), 'b-')
    axs[0].set_title(f'{title} (XY projection)')
    axs[0].set_xlabel('X')
    axs[0].set_ylabel('Y')
    axs[0].axis('equal')

    axs[1].scatter(vertices[:, 0], vertices[:, 2])
    for i in range(len(vertices)):
        for j in range(i + 1, len(vertices)):
            if np.sum(np.abs(vertices[i] - vertices[j]) == 1) == 1:
                axs[1].plot(*zip(vertices[i, [0, 2]], vertices[j, [0, 2]]), 'b-')
    axs[1].set_title(f'{title} (XZ projection)')
    axs[1].set_xlabel('X')
    axs[1].set_ylabel('Z')
    axs[1].axis('equal')

    axs[2].scatter(vertices[:, 1], vertices[:, 2])
    for i in range(len(vertices)):
        for j in range(i + 1, len(vertices)):
            if np.sum(np.abs(vertices[i] - vertices[j]) == 1) == 1:
                axs[2].plot(*zip(vertices[i, 1:], vertices[j, 1:]), 'b-')
    axs[2].set_title(f'{title} (YZ projection)')
    axs[2].set_xlabel('Y')
    axs[2].set_ylabel('Z')
    axs[2].axis('equal')

    plt.show()

scaling_matrix = np.array([
    [2, 0, 0],
    [0, 1, 0],
    [0, 0, 0.5]
])
scaled_vertices = cube_vertices @ scaling_matrix.T
plot_cube(scaled_vertices, "Масштабування")

theta = np.pi / 4  # 45 градусів
rotation_matrix = np.array([
    [np.cos(theta), -np.sin(theta), 0],
    [np.sin(theta), np.cos(theta), 0],
    [0, 0, 1]
])
rotated_vertices = cube_vertices @ rotation_matrix.T
plot_cube(rotated_vertices, "Обертання")
