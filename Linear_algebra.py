import numpy as np
import matplotlib.pyplot as plt

points_1 = np.array([
    [0, 1, 2, 1.5, 3, 1.5, 1, 0.5, -1, 0.5, 0],
    [0, 1, 0, 0.7, 1.8, 2.5, 1.2, 2, 1.8, 0.6, 0]
])

fish_coordinates = np.array([
    [-3.5, 0.5], [-3, 2], [-2, 3], [-1, 3], [0, 2], [2, 2.5], [3, 2], [3.5, 2.5], [4, 1.5],
    [3.5, 0.5], [3, 0.5], [3.5, 0], [3, -0.5], [2.5, 0], [2.5, -1], [3, -2], [2.5, -3.5],
    [2, -3], [2, -2], [1, -2.5], [0.5, -3], [0.5, -4.5], [-0.5, -4.5], [-0.5, -3.5],
    [-1.5, -3.5], [-1.5, -5], [-2, -6], [-3.5, -4.5], [-2.5, -3.5], [-4, -4],
    [-4, -2.5], [-2.5, -2.5], [-1.5, 0], [-2.5, 1.5], [-3.5, 0.5]
])

def plot_object(points, title):
    plt.figure(figsize=(5, 5))
    plt.plot(points[0, :], points[1, :], 'o-')
    plt.title(title)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True)
    plt.show()


def plot_fish(coords, title):
    x_coords, y_coords = zip(*coords)
    fig, ax = plt.subplots()
    ax.plot(x_coords, y_coords, marker='o', linestyle='-', color='black')
    ax.fill_between(x_coords, y_coords, color='skyblue', alpha=0.3)
    ax.grid(True, which='both')
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    ax.set_aspect('equal', 'box')
    plt.xlim(-6, 6)
    plt.ylim(-7, 4)
    plt.title(title)
    plt.show()


def rotate(points, angle):
    theta = np.radians(angle)
    rotation_matrix = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta), np.cos(theta)]
    ])
    return np.dot(rotation_matrix, points)


def scale(points, scale_factor):
    scale_matrix = np.array([
        [scale_factor, 0],
        [0, scale_factor]
    ])
    return np.dot(scale_matrix, points)


def reflect(points, axis):
    if axis == 'x':
        reflect_matrix = np.array([
            [1, 0],
            [0, -1]
        ])
    elif axis == 'y':
        reflect_matrix = np.array([
            [-1, 0],
            [0, 1]
        ])
    return np.dot(reflect_matrix, points)


def shear(points, shear_factor, axis):
    if axis == 'x':
        shear_matrix = np.array([
            [1, shear_factor],
            [0, 1]
        ])
    elif axis == 'y':
        shear_matrix = np.array([
            [1, 0],
            [shear_factor, 1]
        ])
    return np.dot(shear_matrix, points)


def custom_transform(points, transform_matrix):
    return np.dot(transform_matrix, points)


plot_object(points_1, "Original Object")
plot_fish(fish_coordinates, "Original Fish")

print("Star")

rotated_points = rotate(points_1, 45)
plot_object(rotated_points, "Rotated Object (45 degrees)")
print("Rotation Matrix (45 degrees):")
print(rotate(np.eye(2), 45))

scaled_points = scale(points_1, 1.5)
plot_object(scaled_points, "Scaled Object (1.5x)")
print("Scaling Matrix (1.5x):")
print(scale(np.eye(2), 1.5))

reflected_points_x = reflect(points_1, 'x')
plot_object(reflected_points_x, "Reflected Object (x-axis)")
print("Reflection Matrix (x-axis):")
print(reflect(np.eye(2), 'x'))

sheared_points_x = shear(points_1, 1, 'x')
plot_object(sheared_points_x, "Sheared Object (x-axis)")
print("Shearing Matrix (x-axis):")
print(shear(np.eye(2), 1, 'x'))

custom_matrix = np.array([
    [1, 0.5],
    [0.5, 1]
])
custom_transformed_points = custom_transform(points_1, custom_matrix)
plot_object(custom_transformed_points, "Custom Transformed Object")
print("Custom Transformation Matrix:")
print(custom_matrix)

print("\nFish")

rotated_fish = rotate(fish_coordinates.T, 45).T
plot_fish(rotated_fish, "Rotated Fish (45 degrees)")

scaled_fish = scale(fish_coordinates.T, 1.5).T
plot_fish(scaled_fish, "Scaled Fish (1.5x)")

reflected_fish_x = reflect(fish_coordinates.T, 'x').T
plot_fish(reflected_fish_x, "Reflected Fish (x-axis)")

sheared_fish_x = shear(fish_coordinates.T, 1, 'x').T
plot_fish(sheared_fish_x, "Sheared Fish (x-axis)")

custom_transformed_fish = custom_transform(fish_coordinates.T, custom_matrix).T
plot_fish(custom_transformed_fish, "Custom Transformed Fish")
