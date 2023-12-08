from loops import *
from recursion import *

print("Factorial of 6 using a loop is:", loops.factorial(6))
print("Factorial of 5 using a loop is:", loops.factorial(5))
print("Factorial of 1 using a loop is:", loops.factorial(1))

print("Factorial of 6 using a loop is:", recursion.factorial(6))
print("Factorial of 5 using a loop is:", recursion.factorial(5))
print("Factorial of 1 using a loop is:", recursion.factorial(1))

print("2 to the 5th power using a loop is:", loops.power(2, 5))
print("2 to the 4th power using a loop is:", loops.power(2, 4))
print("2 to the 0 power using a loop is:", loops.power(2, 0))

print("2 to the 5th power using a loop is:", recursion.power(2, 5))
print("2 to the 4th power using a loop is:", recursion.power(2, 4))
print("2 to the 0 power using a loop is:", recursion.power(2, 0))

nums = [5,12,3,4]
print("Minimum number using a loop is:", loops.computeMin(nums))
print("Minimum number using recursion is:", recursion.computeMin(nums, 0, nums[0]))

str = "Hello World"
loops.reverse(str)
recursion.reverse(str, len(str))


### Module 8 Major Assignment A
#Test with loop
a = []
first = 0
size = 0
target = 0

#prompt the user for the elements and input them into a list
a = list(map(int, input('Enter seven numbers separated by a space: ').split()))

#prompt the user for the index at which the search will begin
first = int(input('Enter the index at which the search will begin: '))

#prompt the user for the number of elements to search 
size = int(input('Enter the size of the list that will be searched: '))

#prompt the user for the target
target = int(input('Enter the target value to search for: '))

#call search and display its return
print('Target found at index ... ', loops.search(a, first, size, target))


# Test with Recursion
a = []
first = 0
size = 0
target = 0

#prompt the user for the elements and input them into a list
a = list(map(int, input('Enter seven numbers separated by a space: ').split()))

#prompt the user for the index at which the search will begin
first = int(input('Enter the index at which the search will begin: '))

#prompt the user for the number of elements to search 
size = int(input('Enter the size of the list that will be searched: '))

#prompt the user for the target
target = int(input('Enter the target value to search for: '))

#call search and display its return
print(recursion.search(a, first, size, target, 0, False))


