import numpy as np
import matplotlib.pyplot as plt

# Image size (pixels)
width, height = 800, 800

# Plot window (complex plane)
real_min, real_max = -2.0, 1.0
imag_min, imag_max = -1.5, 1.5

# Maximum number of iterations
max_iter = 256

# Create a grid of complex numbers
real = np.linspace(real_min, real_max, width)
imag = np.linspace(imag_min, imag_max, height)
complex_grid = real[np.newaxis, :] + imag[:, np.newaxis] * 1j

# Initialize the Mandelbrot set array
mandelbrot_set = np.zeros(complex_grid.shape, dtype=int)

# Compute Mandelbrot set
z = np.zeros(complex_grid.shape, dtype=complex)
for i in range(max_iter):
    mask = np.abs(z) <= 2
    z[mask] = z[mask]**2 + complex_grid[mask]
    mandelbrot_set[mask] = i

# Plot the Mandelbrot set
plt.figure(figsize=(10, 10))
plt.imshow(mandelbrot_set, extent=(real_min, real_max, imag_min, imag_max), cmap="hot")
plt.colorbar(label="Iterations")
plt.title("Mandelbrot Set")
plt.xlabel("Re (Real)")
plt.ylabel("Im (Imaginary)")
plt.savefig("mandelbrot.png")  # Save as a PNG image
plt.show()