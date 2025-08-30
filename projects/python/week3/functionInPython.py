## addNumbers function

def addNumbers(num1, num2):
    return num1 + num2

input1 = float(input("Enter your first number: "))
input2 = float(input("Enter your second number: "))

sum = addNumbers(input1, input2)
print ("The sum is:", sum)

## isEven function

def isEven(givenNum):
    if givenNum % 2 == 0:
        return True
    else:
        return False
    
number = int(input("Enter an even or odd number: "))

if isEven(number):
    print("The number is even")
else:
    print("The number is odd")

## greet function

def greet(name = "Guest"):
    print("Hello,", name)

userName = input("Enter your name: ")
greet(userName)
greet() #calls greet with default parameter

##factorial function

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
num = int(input("Enter a non-negative integer: "))

factorialResult = factorial(num)
print("The factorial of is ", num, "is:", factorialResult)
