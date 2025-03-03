#Assignments 1
#1. Write a function to return the grade based on percentage
#Solution:
def getGrade(perc):
 if perc < 35:
grade ="Fail"
elif perc >= 35 and perc <= 50:
grade = "Third div"
elif perc >50 and perc<65:
grade = 'Second div'
else:
grade = "First div"
return grade
perc = input("Enter the percetage :")
print("Your garde is : ",getGrade(int(perc)))
#2. Write a function that return a list of common elements from two different sets
#Solution:
def findCommonElement(set1, set2):
 set3 = set1 & set2
return set3
set1 = {1,2,3,4,5}
set2 = {1,4,5,8,9}
print(findCommonElement(set1,set2))
#3. Convert a String to a List of Characters
#Solution:
def convertStringToList(s):
 return list(s)
s = input("Enter a string : ")
print(convertStringToList(s))
#4. Write a function to check if list contains any duplicate element and return “Yes” or
#“No” as application
# Check if my List contains any duplicate element
#Solution:
def checkDuplicateInList(lst):
 set1 = set(lst)
if(len(set1) == len(lst)):
return False
else:
return True
lst = [1,2,3,4,5,20,1]
ans = checkDuplicateInList(lst)
print(ans)
#5. Given a list, write a function that provide the occurrence of element against each
#element in the list.
#e.g. List = [1,2,3,4,5,1,3]
#Expected Output:
#1: 2
#2:1
#3: 2
#4: 1
#5: 1
#Solution: def count_elements(input_list):
counts = {}
for element in input_list:
 if element in counts:
counts[element] += 1
else:
counts[element] = 1
return counts
# Example usage:
my_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
result = count_elements(my_list)
print(result)
#6. Write a function return a substring where it starts from 2rd occurrence of ‘a’ and end
#at 2nd occurrent of ‘b’
e.g. s = "abracadabra"
start_char = 'a'
end_char = 'b'
#Solution:
def find_substring(s, start_char, end_char):
# Find the 2nd occurrence of start_char
first_index = s.find(start_char)
if first_index == -1:
return '' # Not found
second_index = s.find(start_char, first_index + 1)
if second_index == -1:
return '' # Only one occurrence found
# Find the 2nd occurrence of end_char
first_index_b = s.find(end_char)
if first_index_b == -1:
return '' # Not found
second_index_b = s.find(end_char, first_index_b + 1)
if second_index_b == -1:
return '' # Only one occurrence found
# Extract and return the substring
return s[second_index:second_index_b + 1]
# Example usage:
s = "abracadabra"
start_char = 'a'
end_char = 'b'
result = find_substring(s, start_char, end_char)
print(result) # Output: "acadab"
#Assignments 2
#1. Given a string , write a python code to reverse the string using for loop and slice
#operator both
#ways?
Input: city = "ETLQALabs"
#expected output: “sbaL AQ LTE”
#1. Using a for loop
# Input string
city = "ETLQALabs"
# Reversing using a for loop
reversed_for_loop = ''
for char in city:
 reversed_for_loop = char + reversed_for_loop
print(reversed_for_loop) # Output: "sbaL AQ LTE"
#2. Using the slice operator
# Input string
city = "ETLQALabs"
# Reversing using slicing
reversed_slicing = city[::-1]
print(reversed_slicing) # Output: "sbaL AQ LTE"
#2. Extract a substring form character "Q" and ends at "b"
Input: city = "ETLQALabs"
#Expected O/P : QAlab
#Code
# Input string
city = "ETLQALabs"
# Find the starting index of 'Q'
start_index = city.find("Q")
# Find the ending index of 'b' (inclusive)
end_index = city.find("b")
# Extracting the substring
if start_index != -1 and end_index != -1:
 substring = city[start_index:end_index + 1]
else:
 substring = '' # Handle cases where 'Q' or 'b' is not found
print(substring) # Output: "QALab"
#3. Write a python code to check if the given list contains duplicate elements and
#print yes or no as
#per input
#e.g.
#list1 =[1,2,3,4,3] => Yes
#list2 =[1,2,3,4] => No
#Code:
def check_duplicates(input_list):
# Convert the list to a set to remove duplicates
unique_elements = set(input_list)
# Compare lengths to check for duplicates
if len(unique_elements) < len(input_list):
return "Yes" # There are duplicates
else:
return "No" # No duplicates
# Example usage
list1 = [1, 2, 3, 4, 3]
list2 = [1, 2, 3, 4]
print(check_duplicates(list1)) # Output: Yes
print(check_duplicates(list2)) # Output: No
#4. How would you use slicing to create a new list containing only the odd-indexed
#elements of a
#given list?
#Input : list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#Expected output : [1, 3, 5, 7, 9]
#Code:
# Input list
input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Slicing to get odd-indexed elements
odd_indexed_elements = input_list[1::2]
# Print the result
print(odd_indexed_elements) # Output: [1, 3, 5, 7, 9]
#5. How would you use slicing to create a new list containing only the even-indexed
#elements of a
#given list?
#Input : list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#Expected output : [0, 2, 4, 6, 8]
#Code:
# Input list
input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Slicing to get even-indexed elements
even_indexed_elements = input_list[0::2]
# Print the result
print(even_indexed_elements) # Output: [0, 2, 4, 6, 8]