## Division program that hands division by zero exception.

try:
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
    result = numerator / denominator
    print("The result is:", result)
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")

## Division program that handles zero & value errors.

numeric = False

while not numeric:
    try:
        num1 = float(input("Enter the numerator: "))
        num2 = float(input("Enter the denominator: "))
        result = num1 / num2
        print("The result is:", result)
        numeric = True
    except ZeroDivisionError:
        print("Error: You cannot divide by zero")
    except ValueError:
        print("Error: Invalid input, please enter numeric values.")

## Using finally to detemine valid input.

try:
    userInput = float(input("Enter a number: "))
    print("You entered:", userInput)
except ValueError:
    print("Error: Invalid input, please enter numeric values.")
finally:
    print("Execution completed.")