def f(x, y, b):
    return ((-2 * y) / x) + (2 / (3 * x)) - ((4 * b * x) / 3)

def euler(x0, y0, h, x, decimal, b):
    n = int((x - x0) / h)
    y = y0
    print("*" * 50)
    print("Iteration\t\t x\t\t y")
    print("-" * 50)
    for i in range(n):
        y = y + h * f(x0, y, b)  # Pass b as an argument to the function
        x0 = x0 + h
        print(f"{i + 1}\t\t\t {x0:.{decimal}f}\t\t {y:.{decimal}f}")
    print("*" * 50)
    print(f"The approximate value of y at x = {x:.{decimal}f} is {y:.{decimal}f}")

def main():
    try:
        print("*" * 50)
        print("Welcome to Euler Method")
        print("*" * 50)
        x0 = float(input("Enter the initial value of x: "))
        y0 = float(input("Enter the initial value of y: "))
        h = float(input("Enter the step-size: "))
        x = float(input("Enter the value of x at which y is to be found: "))
        decimal = int(input("Enter the number of decimal places to be displayed: "))
        b = float(input("Enter the value of b: ")) # Ask the user to enter the value of b 

        euler(x0, y0, h, x, decimal, b)

        # Ask the user if they want to enter values again
        repeat = input("Do you want to enter values again? (yes/no): ").lower() # Convert the input to lowercase for consistency    
        if repeat == 'yes':
            main()  # Call main function again
        else:
            print("Exiting program.") # Print a message to indicate that the program is exiting
    except ValueError: # Handle the ValueError exception that occurs when the user enters invalid input 
        print("Invalid input. Please enter numerical values.")

if __name__ == "__main__":
    main()
