def grams_to_ounces(grams):
    ounces_per_gram = 1 / 28.3495231
    return grams * ounces_per_gram
def fahrenheit_to_celsius():
    
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    

    celsius = (5.0 / 9.0) * (fahrenheit - 32)
    
    print(f"{fahrenheit} Fahrenheit is equivalent to {celsius:.2f} Celsius.")

def solve(numheads, numlegs):
    for rabbits in range(numheads + 1):
        chickens = numheads - rabbits
        if 2 * chickens + 4 * rabbits == numlegs:
            print(f"Rabbits: {rabbits}, Chickens: {chickens}")
            return
    print("No valid solution.")
def is_prime(n):
    if n <= 1:
        return False
    
    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    
    return True

def filter_prime(numbers):
    """
    Return a list of prime numbers from the given list of integers.
    """
    return [num for num in numbers if is_prime(num)]

if __name__ == "__main__":
    nums = [2, 3, 4, 5, 10, 13, 17, 20, 23, 29, 33]
    prime_nums = filter_prime(nums)

    print("Original list:", nums)
    print("Prime numbers:", prime_nums)
def print_permutations(s, prefix=""):
    if len(s) == 0:
        print(prefix)
    else:
        for i in range(len(s)):
            print_permutations(s[:i] + s[i+1:], prefix + s[i])

x = input()
print_permutations(x)
def reverse_words(sentence):
    return " ".join(sentence.split()[::-1])

x = input()
print(reverse_words(x))

def has_33(nums):
    return any(nums[i] == 3 and nums[i + 1] == 3 for i in range(len(nums) - 1))

x = list(map(int, input().split()))
print(has_33(x))

import math

def sphere_volume(radius):
    return (4/3) * math.pi * radius**3

r = float(input())
print(sphere_volume(r))

def unique_elements(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

x = list(map(int, input().split()))
print(unique_elements(x))

def is_palindrome(s):
    cleaned = "".join(s.lower().split())
    return cleaned == cleaned[::-1]

x = input()
print(is_palindrome(x))

def histogram(lst):
    for num in lst:
        print('*' * num)

x = list(map(int, input().split()))
histogram(x)

import random

def guess_the_number():
    number_to_guess = random.randint(1, 20)
    attempts = 0

    print("I am thinking of a number between 1 and 20.")
    
    while True:
        guess = int(input("Take a guess: "))
        attempts += 1

        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            print(f"Good job! You guessed my number in {attempts} guesses!")
            break

guess_the_number()

# utilities.py

import math
import random

def sphere_volume(radius):
    return (4/3) * math.pi * radius**3

def is_palindrome(s):
    cleaned = "".join(s.lower().split())
    return cleaned == cleaned[::-1]

def unique_elements(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

def histogram(lst):
    for num in lst:
        print('*' * num)

def has_33(nums):
    return any(nums[i] == 3 and nums[i + 1] == 3 for i in range(len(nums) - 1))

def guess_the_number():
    number_to_guess = random.randint(1, 20)
    attempts = 0
    print("I am thinking of a number between 1 and 20.")
    
    while True:
        guess = int(input("Take a guess: "))
        attempts += 1

        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            print(f"Good job! You guessed my number in {attempts} guesses!")
            break

# main.py

from utilities import sphere_volume, is_palindrome, unique_elements, histogram, has_33

print("Sphere Volume of radius 3:", sphere_volume(3))

word = "madam"
print(f"Is '{word}' a palindrome? {is_palindrome(word)}")

numbers = [1, 2, 2, 3, 4, 4, 5]
print("Unique elements:", unique_elements(numbers))

print("Histogram for [3, 5, 2]:")
histogram([3, 5, 2])

num_list = [1, 3, 3, 4, 5]
print("Has consecutive 3s?", has_33(num_list))
