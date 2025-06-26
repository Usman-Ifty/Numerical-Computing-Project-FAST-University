import numpy as np # Import numpy library as np alias 
import matplotlib.pyplot as plt # Import matplotlib.pyplot library as plt alias 

def f(x, y): # Define a function f(x, y) that takes two arguments x and y 
    return ((-2 * y) / x) + (2 / (3 * x)) - ((4 * x) / 3)   # Return the value of the differential equation at a given point (x, y)    

def euler(x0, y0, h, x): # Define a function euler that takes four arguments x0, y0, h, and x
    n = int((x - x0) / h)   # Calculate the number of steps required to reach the final value of x
    x_values = [x0] # Initialize the list of x values with the initial value x0
    y_values = [y0] # Initialize the list of y values with the initial value y0 
    for i in range(n): # Iterate over the range of values from 0 to n
        y0 = y0 + h * f(x0, y0) # Update the value of y using Euler's method 
        x0 = x0 + h # Update the value of x by adding the step-size h 
        x_values.append(x0) # Append the new value of x to the list of x values
        y_values.append(y0) # Append the new value of y to the list of y values 
        #where is the value of y being appended to the list of y_values?
        #The new value of y is being appended to the list y_values in the line y_values.append(y0). This line of code appends the updated value of y to the list y_values after each iteration of the loop.
    return np.array(x_values), np.array(y_values) # Return the x and y values as numpy arrays 
#why are the x_values and y_values being returned as numpy arrays?
#The x_values and y_values are being returned as numpy arrays to facilitate further processing and analysis of the data. Numpy arrays provide efficient storage and manipulation of numerical data, making them suitable for scientific computing tasks.

def runge_kutta(x0, y0, h, x):
    n = int((x - x0) / h)
    x_values = [x0]
    y_values = [y0]
    for i in range(n):
        k1 = h * f(x0, y0)
        k2 = h * f(x0 + 0.5 * h, y0 + 0.5 * k1)
        k3 = h * f(x0 + 0.5 * h, y0 + 0.5 * k2)
        k4 = h * f(x0 + h, y0 + k3)
        y0 = y0 + (1.0 / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
        x0 = x0 + h
        x_values.append(x0) # Append the new value of x to the list of x values
        y_values.append(y0) # Append the new value of y to the list of y values
    return np.array(x_values), np.array(y_values) # Return the x and y values as numpy arrays 

def main():
    try:
        print("*" * 50)
        print("Welcome to the Comparison of Euler and Runge-Kutta Methods")
        print("*" * 50)
        x0 = float(input("Enter the initial value of x: "))
        y0 = float(input("Enter the initial value of y: "))
        h = float(input("Enter the step-size: "))
        x = float(input("Enter the value of x at which y is to be found: "))

        x_values_euler, y_values_euler = euler(x0, y0, h, x) # Call the euler function to calculate the solution using Euler's method
        x_values_rk, y_values_rk = runge_kutta(x0, y0, h, x) # Call the runge_kutta function to calculate the solution using Runge-Kutta method 
        #what is the purpose of the np.array() function?
        #The np.array() function is used to create a numpy array from a list of values. In this context, it is used to convert the lists of x and y values into numpy arrays for further processing and analysis.

        #how x_values_euler, y_values_euler and x_values_rk, y_values_rk are being used?
        #The x_values_euler, y_values_euler, x_values_rk, and y_values_rk arrays are being used to store the x and y values obtained from the Euler and Runge-Kutta methods, respectively. These arrays are then used to display the results and plot the solutions.

        print("*" * 50)
        print("Euler Method")
        print("x\t\t y")
        for i in range(len(x_values_euler)): # Iterate over the range of values from 0 to the length of x_values_euler
            print(f"{x_values_euler[i]:.4f}\t\t {y_values_euler[i]:.4f}") # Print the x and y values with 4 decimal places 
        print("*" * 50)
        print("Runge-Kutta Method")
        print("x\t\t y")
        for i in range(len(x_values_rk)): # Iterate over the range of values from 0 to the length of x_values_rk
            print(f"{x_values_rk[i]:.4f}\t\t {y_values_rk[i]:.4f}")
        print("*" * 50)

        plt.plot(x_values_euler, y_values_euler, label='Euler Method') # Plot the solution obtained using Euler's method
        plt.plot(x_values_rk, y_values_rk, label='Runge-Kutta Method') # Plot the solution obtained using Runge-Kutta method

        plt.xlabel('x') # Set the x-axis label to 'x' 
        plt.ylabel('y') # Set the y-axis label to 'y' 
        plt.title('Comparison of Euler and Runge-Kutta Methods') # Set the title of the plot to 'Comparison of Euler and Runge-Kutta Methods'
        plt.legend() # Display the legend in the plot 
        #what is the purpose of the plt.legend() function?
        #The plt.legend() function is used to display the legend in the plot. The legend provides information about the data being plotted, such as the labels associated with each line or marker in the plot

        plt.grid(True) # Display the grid in the plot
        plt.show()  # Display the plot

        # Write the solution data to a file
        with open("solution.txt", "w") as file:
            file.write("x\tEuler Method\tRunge-Kutta Method\n")
            for i in range(len(x_values_euler)):
                file.write(f"{x_values_euler[i]:.4f}\t{y_values_euler[i]:.4f}\t{y_values_rk[i]:.4f}\n")

        # Ask the user if they want to run the program again
        repeat = input("Do you want to enter values again? (yes/no): ").lower()
        if repeat == 'yes':
            main()  # Call main function again
        else:
            print("Exiting program.")
    except ValueError:
        print("Invalid input. Please enter numerical values.")

if __name__ == "__main__":
    main()
