import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

def load_data(filename):
    """Load data from a file."""
    data = np.loadtxt(filename)  # Load the data from the file
    x = data[:, 0]  # Extract the x values from the first column of the data
    y = data[:, 1]  # Extract the y values from the second column of the data
    return x, y

def interpolate_cubic_spline(x, y):
    """Perform cubic spline interpolation."""
    cs = CubicSpline(x, y)  # Create a CubicSpline object with the x and y values
    x_interp = np.linspace(min(x), max(x), 1000)  # Generate 1000 points for interpolation between the minimum and maximum x values
    y_interp = cs(x_interp)  # Perform cubic spline interpolation on the x_interp values
    return x_interp, y_interp

def plot_interpolation(x, y, x_interp, y_interp):
    """Plot the original data and the interpolated data."""
    plt.figure(figsize=(10, 6))  # Set the size of the plot
    plt.scatter(x, y, color='red', label='Original Data')  # Plot the original data points
    plt.plot(x_interp, y_interp, color='blue', label='Interpolated Data')  # Plot the interpolated data
    plt.xlabel('x')  # Set the x-axis label
    plt.ylabel('y')  # Set the y-axis label
    plt.title('Cubic Spline Interpolation')  # Set the title of the plot
    plt.legend()  # Display the legend
    plt.grid(True)  # Display the grid
    plt.show()  # Display the plot

def main():
    filename = 'bps.dat'  # File containing the data
    x, y = load_data(filename)
    x_interp, y_interp = interpolate_cubic_spline(x, y)
    plot_interpolation(x, y, x_interp, y_interp)

if __name__ == "__main__":
    main()
