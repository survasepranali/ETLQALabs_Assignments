#Assignments
#1. Write a Python program using function that calculates the factorial of a given number n (n!) using
#both a for loop and a while loop.
#Example:
Input: n = 4
Output: 24
#Explanation: (4! = 4 × 3 × 2 × 1 = 24)
#Solution
# Solution using for loop
def get_factorial_using_for_loop(num):
 ans = 1
for i in range(1, num + 1):
ans *= i
return ans
# Solution using for while
def get_factorial_using_while_loop(num):
ans = 1
i = 1
while i <= num:
 ans *= i
i += 1
return ans
# Calling Functions
num = 4
print(f"Factorial of {num} using for loop = {get_factorial_using_for_loop(num)}")
print(f"Factorial of {num} using while loop= {get_factorial_using_while_loop(num)}")
#2. Write a Python program that finds and prints all the prime numbers between 1 and N using both a
#for loop and a while loop.
#Example :
Input: N = 10
Output: 2 3 5 7
#Explanation: (Prime numbers between 1 and 10 are 2, 3, 5, and 7)
#Solution
# Solution Using a for loop
def get_prime_numbers_using_for(num):
 list_of_prime_numbers = []
for i in range(2, num + 1):
 is_prime_number = True
for j in range(2, i): # Check all numbers from 2 to i-1
 if i % j == 0:
is_prime_number = False
break
if is_prime_number:
 list_of_prime_numbers.append(i)
return list_of_prime_numbers
# Solution Using a while loop
def get_prime_numbers_using_while(num):
 list_of_prime_numbers = []
i = 2
while i <= num:
 is_prime_number = True
for j in range(2, i): # Check all numbers from 2 to i-1
 if i % j == 0:
is_prime_number = False
break
if is_prime_number:
 list_of_prime_numbers.append(i)
i += 1
return list_of_prime_numbers
# Calling/executing functions
num = 10
print(f"Prime numbers between 1 and {num} using for loop: {get_prime_numbers_using_for(num)}")
print(f"Prime numbers between 1 and {num} using while loop:
{get_prime_numbers_using_while(num)}")
#3. Write a Python program that counts the number of digits in a given number using both a for loop
#and a while loop.
#Example :
Input: n = 12345
Output: 5
#Explanation: (Number of digits in 12345 is 5)
#Solution
# Function to count digits using a for loop
def count_digits_using_for_loop(num):
count_of_digits = 0
for digit in str(num): # Convert number to string and iterate through each character
 count_of_digits += 1
return count_of_digits
# Function to count digits using a while loop
def count_digits_using_while_loop(num):
 count_of_digits = 0
while num != 0:
 num = num // 10 # Remove the last digit of the number
count_of_digits += 1
return count_of_digits
# Input
num = 12345
# Calling the functions
print("Number of digits using for loop):", count_digits_using_for_loop(num))
print("Number of digits using while loop):", count_digits_using_while_loop(num))
#4. Write a Python program that calculates the sum of the first N natural numbers (1 + 2 + 3 + ... + N)
#using both a for loop and a while loop.
#Example
Input: N = 5
Output: 15
#Explanation: (Sum of 1 + 2 + 3 + 4 + 5 = 15)
#Solution
# Function to calculate sum using a for loop
def sum_of_n_natural_number_using_for_loop(num):
total = 0
for i in range(1, num+1):
 total += i
return total
# Function to calculate sum using a while loop
def sum_of_n_natural_number_using_while_loop(num):
total = 0
i = 1
while i <= num:
 total += i
i += 1
return total
# Taking inputs dynamically
num = int(input("Enter a number : "))
# Output
print("Sum of natural number using for loop:", sum_of_n_natural_number_using_for_loop(num))
print("Sum of natural number using while loop:",
sum_of_n_natural_number_using_while_loop(num))
#5. Write a Python program that generates the Fibonacci series up to N terms using both a for
#loop and a while loop.
#Example
Input: N = 6
Output: 0 1 1 2 3 5
#Explanation: (The first 6 terms of the Fibonacci series are 0, 1, 1, 2, 3, and 5)
#Solution
def fibonacci_series_using_for_loop(num):
 fib_series_list = []
a, b = 0, 1
for i in range(num):
 fib_series_list.append(a)
temp = a
a = b
b = temp + b
return fib_series_list
def fibonacci_series_using_while_loop(num):
fib_series_list = []
a, b = 0, 1
count = 0
while count < num:
 fib_series_list.append(a)
# a, b = b, a + b -> as we can write in this way or using temp
temp = a
a = b
b = temp + b
count += 1
return fib_series_list
num = int(input("Enter the number of terms N: "))
print("Fibonacci series using for loop:", " ".join(map(str, fibonacci_series_using_for_loop(num))))
print("Fibonacci series using while loop:", " ".join(map(str, fibonacci_series_using_while_loop(num))))