import numpy as np # Import numpy library as np alias 

def f(x): # Define a function f(x) that takes a single argument x   
    return x**2 - 5 # Return the value of x^2 - 5
 
def df(x): # Define a function df(x) that takes a single argument x
    return 2 * x # Return the derivative of f(x) which is 2x

def newton_raphson(x0, tol, decimal): # Define a function newton_raphson that takes three arguments x0, tol, and decimal
    #tolerance is the maximum error allowed in the final answer 

    x1 = x0 - f(x0) / df(x0) # Calculate the next value of x using the formula x1 = x0 - f(x0) / f'(x0)
    while abs(x1 - x0) > tol: # Repeat the process until the difference between x1 and x0 is less than the tolerance
        #abs() function returns the absolute value of a number
        #why x1 - x0? because we want to find the difference between the two values
        x0 = x1 # Update the value of x0 to x1 for the next iteration 
        x1 = x0 - f(x0) / df(x0) # Calculate the next value of x using the formula x1 = x0 - f(x0) / f'(x0)
        print("-" * 30) # Print a line of dashes for better readability     
        print("x0\tx1\t f(x1)") # Print the column headers
        print("{:.4f}\t{:.4f}\t{:.4f}".format(x0, x1, f(x1))) # Print the values of x0, x1, and f(x1) with 4 decimal places
        #what is the format() function? It is used to format the output in a specific way
        #what is {:.4f}? It is a placeholder that specifies that the value should be formatted as a floating-point number with 4 decimal places
        print("-" * 30)
        # only return up to user input decimal places
        x1 = round(x1, decimal) # Round the value of x1 to the specified number of decimal places

    return x1 # Return the final value of x1 as the root of the equation

# Main program
print("*" * 50) 
print("Welcome to Newton Raphson Method")
print("*" * 50)

while True: # Repeat the process until the user decides to exit
    try: # Handle any potential errors that may occur during the execution of the program
        x0 = float(input("Enter the initial guess: ")) 
        tol = float(input("Enter the tolerance: "))
        decimal = int(input("Enter the decimal places you want to return: "))
        # call the function
        root = newton_raphson(x0, tol, decimal)
        print("The root of the equation is:", root)
        print("*" * 50)
        
        cont = input("Do you want to find another root? (yes/no): ").lower() # Ask the user if they want to find another root and convert the input to lowercase for consistency 
        if cont != 'yes':
            break  # Exit the loop if the user doesn't want to continue
    except ValueError: # Handle the ValueError exception that occurs when the user enters invalid input 
        print("Invalid input. Please enter numerical values.") 