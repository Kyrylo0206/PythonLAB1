import cv2
import numpy as np
import matplotlib.pyplot as plt

square_vertices = np.array([
    [0, 0],
    [1, 0],
    [1, 1],
    [0, 1]
])

def plot_square(vertices, ax, title):
    ax.scatter(vertices[:, 0], vertices[:, 1])
    ax.plot(*zip(*vertices, vertices[0]), 'b-')
    ax.set_title(title)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.axis('equal')

fig, axs = plt.subplots(1, 2, figsize=(12, 6))

# Corrected scaling matrix for cv2.transform (2x3 matrix)
scaling_matrix = np.array([
    [2, 0, 0],
    [0, 0.5, 0]
], dtype=np.float32)

scaled_vertices = cv2.transform(np.array([square_vertices], dtype=np.float32), scaling_matrix)[0]
plot_square(scaled_vertices, axs[0], "Масштабування (OpenCV)")

theta = 45
rotation_matrix = cv2.getRotationMatrix2D((0.5, 0.5), theta, 1.0)
rotated_vertices = cv2.transform(np.array([square_vertices], dtype=np.float32), rotation_matrix[:, :2])[0]
plot_square(rotated_vertices, axs[1], "Обертання (OpenCV)")

plt.show()

image = cv2.imread('images.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Corrected scale matrix and output size
scale_matrix = np.array([
    [0.5, 0, 0],
    [0, 0.5, 0]
], dtype=np.float32)

# Correct size for the scaled image
scaled_image = cv2.warpAffine(image, scale_matrix, (int(image.shape[1] * 0.5), int(image.shape[0] * 0.5)))

theta = 45  # degrees
rotation_matrix = cv2.getRotationMatrix2D((image.shape[1] // 2, image.shape[0] // 2), theta, 1)
rotated_image = cv2.warpAffine(image, rotation_matrix, (image.shape[1], image.shape[0]))

fig, axs = plt.subplots(1, 3, figsize=(18, 6))
axs[0].imshow(image)
axs[0].set_title('Оригінальне зображення')

axs[1].imshow(scaled_image)
axs[1].set_title('Масштабоване зображення')

axs[2].imshow(rotated_image)
axs[2].set_title('Обертання зображення')

for ax in axs:
    ax.axis('off')

plt.show()
