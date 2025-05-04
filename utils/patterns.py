import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_polar_pattern():
    theta = np.linspace(0, 2*np.pi, 360)
    r = np.abs(np.cos(theta))  # simple directional gain pattern

    plt.figure()
    ax = plt.subplot(111, polar=True)
    ax.plot(theta, r)
    ax.set_title("2D Antenna Radiation Pattern", va='bottom')
    plt.savefig("plots/polar_plot.png")

def plot_3d_radiation():
    theta = np.linspace(0, np.pi, 180)
    phi = np.linspace(0, 2*np.pi, 360)
    theta, phi = np.meshgrid(theta, phi)
    
    r = np.abs(np.sin(theta) * np.cos(phi))  # Example radiation function

    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, cmap='viridis', alpha=0.9)
    ax.set_title("3D Antenna Radiation Pattern")
    plt.savefig("plots/3d_pattern.png")
