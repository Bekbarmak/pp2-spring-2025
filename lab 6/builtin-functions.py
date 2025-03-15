# task 1 
# Write a Python program with builtin function to multiply all the numbers in a list
import math

def multiply_list(nums):
    return math.prod(nums)

print(multiply_list([2, 3, 4]))  

# task 2
# Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    return upper, lower

print(count_case("Hello World"))  

# task 3
# Write a Python program with builtin function that checks whether a passed string is palindrome or not.
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("madam"))  
print(is_palindrome("hello"))  

# task 4
# Write a Python program that invoke square root function after specific milliseconds
import time
import math

def delayed_sqrt(num, delay):
    time.sleep(delay / 1000)
    print(f"Square root of {num} after {delay} milliseconds is {math.sqrt(num)}")

delayed_sqrt(25100, 2123)

# task 5
# Write a Python program with builtin function that returns True if all elements of the tuple are true.
def all_true(t):
    return all(t)

print(all_true((True, True, True)))  
print(all_true((True, False, True)))  
