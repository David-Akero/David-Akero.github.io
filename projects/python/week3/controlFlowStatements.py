##Determine largest number among three numbers

    #gets userInput (three numbers).
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

    #compares the three numbers using if, elif and else statements.
if num1 >= num2 and num1 >= num3:
   largest = num1
elif num2 >= num1 and num2 >= num3:
   largest = num2  
else:
   largest = num3

print("The largest number is:", largest)

##Print even numbers from 1 to 20 using for loop and conitinue statement

print("Even numbers from 1 to 20 are:")

for i in range (1,21): #loop from 1 to 20
   if i % 2 != 0: #checks if number is odd
      continue #skips the odd number
   else:
      print(i)
   
      

##Check if number is between 1 and 50 using and operator

userNum =  float(input("Enter a number: "))# gets user input

#checks if number is between 1 and 50
if userNum >= 1 and userNum <= 50:
    print("The number is between 1 and 50")
else:
    print("The number is not between 1 and 50")

##Iterates through list and finds first multiple of 7 using for and break.

numbers = [12, 15, 22, 29, 35, 42, 50] #list of numbers

for num in numbers: #goes through each number in the list
   if num %7 == 0: #checks if number is multiple of 7 and prints it
     print(num)
     break #exits loop when first multiple of 7 is found
   
##prints 10 to 1 using while loop and not operator

count = 10

while not (count == 0): #loops until count is 0
   print(count)
   count -= 1 #decreases count by 1
      







