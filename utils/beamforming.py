import numpy as np
import matplotlib.pyplot as plt

def plot_beamforming():
    N = 8  # Number of antennas
    d = 0.5  # Distance between antennas (in wavelengths)
    theta = np.linspace(-np.pi, np.pi, 1000)

    # Beam at angle theta0
    theta0 = np.pi / 4  # desired beam direction (45 degrees)
    k = 2 * np.pi
    psi = k * d * (np.cos(theta) - np.cos(theta0))

    AF = np.abs(np.sin(N * psi / 2) / np.sin(psi / 2))
    AF = AF / np.max(AF)

    plt.figure()
    plt.plot(np.degrees(theta), AF)
    plt.title("Beamforming Array Factor (θ0 = 45°)")
    plt.xlabel("Angle (Degrees)")
    plt.ylabel("Normalized Gain")
    plt.grid(True)
    plt.savefig("plots/beamforming.png")
