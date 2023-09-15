import numpy as np
import matplotlib.pyplot as plt

# Constants
mu0 = 4 * np.pi * 10**-7  # permeability of free space

# Coil parameters
outer_diameter = 0.177  # meters
windings_radius = 0.063  # meters
current = 3400  # amps
frequency = 2516461  # Hz
voltage = 1000  # volts
impedance = .0300164  # ohms

# Calculation of current density
cross_sectional_area = np.pi * (outer_diameter / 2)**2 - windings_radius**2
current_density = current / cross_sectional_area

# Calculation of magnetic field
x, y, z = np.meshgrid(np.linspace(-5, 5, 60), np.linspace(-5, 5, 15), np.linspace(-5, 5, 15))
Bx = np.zeros_like(x)
By = np.zeros_like(y)
Bz = np.zeros_like(z)

for i in range(x.shape[0]):
    for j in range(y.shape[1]):
        for k in range(z.shape[2]):
            r = np.sqrt(x[i,j,k]**2 + y[i,j,k]**2 + z[i,j,k]**2)
            if r == 0:
                r = 1e-12  # avoid division by zero
            r_hat = np.array([x[i,j,k]/r, y[i,j,k]/r, z[i,j,k]/r])
            Idl = current_density * r * np.array([0, np.cos(frequency * 2 * np.pi * (r/windings_radius)), np.sin(frequency * 2 * np.pi * (r/windings_radius))]) * np.exp(1j * 2 * np.pi * frequency * r/windings_radius)
            B = (mu0 / (4 * np.pi)) * np.cross(Idl, r_hat) / r**2
            Bx[i,j,k] = B[0].real
            By[i,j,k] = B[1].real
            Bz[i,j,k] = B[2].real

# Plot the magnetic field
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.quiver(x, y, z, Bx, By, Bz, length=0.1, normalize=True)
ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_zlabel('Z (m)')
ax.set_title('Magnetic Field from Coil')
plt.show()








