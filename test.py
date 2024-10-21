import numpy as np
import matplotlib.pyplot as plt

# Constants
g = 9.81  # acceleration due to gravity (m/s^2)
rho = 1.225  # air density (kg/m^3)
C_d = 1.2  # drag coefficient
s = 0.1  # side length of the cube (m)
m = 0.5  # mass of the cube (kg)
dt = 0.01  # time step (s)
e = 0.7  # coefficient of restitution (energy loss factor)

# Initialize variables
y = 100.0  # initial height (m)
v = 0.0  # initial velocity (m/s)
positions = []  # to store positions for plotting
velocities = []  # to store velocities for plotting

for t in np.arange(0, 10, dt):
    # Calculate forces
    F_g = m * g  # gravitational force
    A = s ** 2  # cross-sectional area
    F_d = 0.5 * C_d * rho * A * v**2  # drag force

    # Net force
    F_net = F_g - F_d

    # Acceleration
    a = F_net / m

    # Update velocity and position
    v += a * dt
    y -= v * dt  # subtract because y decreases as it falls

    # Check for collision with the ground
    if y <= 0:
        y = 0  # Reset height to ground level
        v = -e * v  # Reverse and reduce velocity based on energy loss

    # Store values
    positions.append(y)
    velocities.append(v)

# Plot results
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(np.arange(0, len(positions) * dt, dt), positions)
plt.title("Falling Cube Simulation with Bouncing")
plt.xlabel("Time (s)")
plt.ylabel("Height (m)")
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(np.arange(0, len(velocities) * dt, dt), velocities)
plt.title("Velocity of the Falling Cube with Bouncing")
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.grid()

plt.tight_layout()
plt.show()
