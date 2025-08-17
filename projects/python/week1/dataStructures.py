#Max & Min values in a list
numbers = [10, 25, 8, 99, 3, 67]
maxValue = max(numbers)
minValue = min(numbers)
print("Max value:", maxValue)
print("Min value:", minValue)

#How many times a number appears in a tuple
numbers = (2,5,3,5,8,5,10)
countOfFive = numbers.count(5)
print("Number 5 appears:", countOfFive, "times")

#Dictionary: Add a new student and remove new student
students = {"Alice": 85, "Bob": 78, "Charlie": 92}
students["George"] = 91 #adding a student
del students ["Bob"] #removing a student
print("Updated students:", students)

#Union, Intersection, and Difference of Sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
union = set1 | set2 
print("Union of sets:", union)
intersection = set1 & set2
print("Intersection of sets:", intersection)
difference = set1 - set2
print("Difference of sets:", difference)