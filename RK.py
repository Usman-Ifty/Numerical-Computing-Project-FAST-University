def f(x, y):
    return ((-2 * y) / x) + (2 / (3 * x)) - ((4 * x) / 3)

def runge_kutta(x0, y0, h, x, decimal):
    n = int((x - x0) / h)
    y = y0
    print("*" * 50)
    print("Iteration\t\t x\t\t y")
    print("-" * 50)
    for i in range(n):
        k1 = h * f(x0, y)
        k2 = h * f(x0 + 0.5 * h, y + 0.5 * k1)
        k3 = h * f(x0 + 0.5 * h, y + 0.5 * k2)
        k4 = h * f(x0 + h, y + k3)
        y = y + (1.0 / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
        x0 = x0 + h
        print(f"{i + 1}\t\t\t {x0:.{decimal}f}\t\t {y:.{decimal}f}") # Display the iteration number, x, and y values with the specified number of decimal places
        #what is y:.{decimal}f doing?
        #The f-string formatting expression y:.{decimal}f is used to format the value of y with a specific number of decimal places. 
    print("*" * 50)
    print(f"The approximate value of y at x = {x:.{decimal}f} is {y:.{decimal}f}")

    
def main():
    try:
        print("*" * 50)
        print("Welcome to Runge-Kutta Method (1st Order ODE RK Method of Order 4)")
        print("*" * 50)
        x0 = float(input("Enter the initial value of x: "))
        y0 = float(input("Enter the initial value of y: "))
        h = float(input("Enter the step-size: "))
        x = float(input("Enter the value of x at which y is to be found: "))
        decimal = int(input("Enter the number of decimal places to be displayed: "))
        
        runge_kutta(x0, y0, h, x, decimal)

        # Ask the user if they want to enter values again
        repeat = input("Do you want to enter values again? (yes/no): ").lower()
        if repeat == 'yes':
            main()  # Call main function again
        else:
            print("Exiting program.")
    except ValueError:
        print("Invalid input. Please enter numerical values.")

if __name__ == "__main__":
    main()
