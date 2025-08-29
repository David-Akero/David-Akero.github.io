## Remainder finder
num1 = int(input("Remainder Finder - Enter first number(dividend): "))
num2 = int(input("Remainder Finder - Enter second number (divisor): "))

remainder = num1 % num2

print ("The remainder when", num1, "is divided by", num2, "is:", remainder)

##greater, less than, or equal to 10
numInput = int(input("#10 Comparison - Enter your number: "))

isGreater = numInput > 10
isLess = numInput < 10
isEqual = numInput == 10  

print("Is your number greater than 10?", isGreater)
print("Is your number less than 10?", isLess) 
print("Is your number equal to 10?", isEqual)

## Check if number is between 1 and 100 (using and)
userInput = int(input("Between 1 and 100 Check - Enter a number:"))

isBetween = userInput >= 1 and userInput <= 100
isNotBetween = not isBetween

print("Is your number between 1 and 100?", isBetween)
print("Is your number not between 1 and 100?", isNotBetween)

## Check if number is not negative (using not)
newUserInput = int(input("Non-Negative Check - Enter a number:"))
isNegative = not ( newUserInput >= 0)
isNonNegative = not isNegative

print("Is your number negative?", isNegative)
print("Is your number non-negative?", isNonNegative)

## Arithmetic operations
userNum = int(input("Arithmetic Operations - Enter a number: "))
userNum += 5
userNum *= 2

print("After adding 5 and multiplying by 2, your number is:", userNum)
