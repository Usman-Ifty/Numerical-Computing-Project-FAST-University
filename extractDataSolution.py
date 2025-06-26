import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return ((-2 * y) / x) + (2 / (3 * x)) - ((4 * x) / 3)

def euler(x0, y0, h, x):
    n = int((x - x0) / h)
    x_values = [x0]
    y_values = [y0]
    for i in range(n):
        y0 = y0 + h * f(x0, y0)
        x0 = x0 + h
        x_values.append(x0)
        y_values.append(y0)
    return np.array(x_values), np.array(y_values)

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
        x_values.append(x0)
        y_values.append(y0)
    return np.array(x_values), np.array(y_values)

def main():
    try:
        print("*" * 50)
        print("Welcome to the Comparison of Euler and Runge-Kutta Methods")
        print("*" * 50)
        x0 = float(input("Enter the initial value of x: "))
        y0 = float(input("Enter the initial value of y: "))
        h = float(input("Enter the step-size: "))
        x = float(input("Enter the value of x at which y is to be found: "))

        x_values_euler, y_values_euler = euler(x0, y0, h, x)
        x_values_rk, y_values_rk = runge_kutta(x0, y0, h, x)

        print("*" * 50)
        print("Euler Method")
        print("x\t\t y")
        for i in range(len(x_values_euler)):
            print(f"{x_values_euler[i]:.4f}\t\t {y_values_euler[i]:.4f}")
        print("*" * 50)
        print("Runge-Kutta Method")
        print("x\t\t y")
        for i in range(len(x_values_rk)):
            print(f"{x_values_rk[i]:.4f}\t\t {y_values_rk[i]:.4f}")
        print("*" * 50)

        plt.plot(x_values_euler, y_values_euler, label='Euler Method')
        plt.plot(x_values_rk, y_values_rk, label='Runge-Kutta Method')

        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Comparison of Euler and Runge-Kutta Methods')
        plt.legend()
        plt.grid(True)
        plt.show()

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
