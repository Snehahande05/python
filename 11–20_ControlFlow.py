# 11.	Largest of Three Numbers
# •	Input three distinct numbers and print the largest
# num1 = int(input("Enter first number:"))
# num2 = int(input("Enter second number:"))
# num3 = int(input("Enter third number:"))
# print(f"The largest number is {max(num1 , num2, num3)}")

# 12.	Leap Year Checker**
# •	Input a year and determine if it’s a leap year.
# year = int(input("Enter the year:"))
# if (year % 4 == 0 ):
#     print(f"The {year} is a leap year")
# else:
#     print(f"The {year} is not a leap year")

# 13.	Multiplication Table
# •	Input a positive integer and print its multiplication table (e.g., 1 to 10).
# num = int(input("Enter the positive integer:"))
# for i in range(1,11):
#     print(f"{num} x {i} = {num * i}")

# 14.	Sum of N Natural Numbers
# •	Input a positive integer n. Calculate the sum of the first n natural numbers.
# num = int(input("Enter a positive integer: "))
# print(f"The sum of first {num} natural numbers is {num * (num + 1) // 2}")

# 15.	Factorial of a Number
# •	Input a non-negative integer and compute its factorial.
# import math
# fact = int(input("Enter the non-negative integer:"))
# print(f"The factorial of {fact} is {math.factorial(fact)}")

# 16.	Number Guessing (While Loop)
# •	Generate a random number. 
# Prompt the user to guess until they get it right.
# import random
# number = random.randint(1, 100)
# guess = None
# while guess != number:
#     guess = int(input("Guess the number (1-100): "))
#     if guess < number:
#         print("Too low!")
#     elif guess > number:
#         print("Too high!")
# print("You guessed it right!")

# 17.	Count Digits of a Number
# •	Input a positive integer and count how many digits it has.
# n = int(input("Enter a positive integer: "))
# print(f"The number of digits in {n} is {len(str(n))}")

# 18.	Reverse a Number (While Loop)
# •	Input a positive integer and reverse its digits (e.g., 123 -> 321).
# n = int(input("Enter a positive integer: "))
# reverse = 0
# while n > 0:
#     reverse = reverse * 10 + n % 10
#     n //= 10
# print(f"The reversed number is {reverse}")

# 19.	Sum of Even and Odd Numbers Separately
# •	Input a positive integer n. 
# Sum up all even numbers and all odd numbers from 1 to n separately.
# num = int(input("Enter a positive integer: "))
# even_sum = sum(i for i in range(1, num + 1) if i % 2 == 0)
# odd_sum = sum(i for i in range(1, num + 1) if i % 2 != 0)
# print(f"Sum of even numbers: {even_sum}")
# print(f"Sum of odd numbers: {odd_sum}")

# 20.	Palindrome Checker (Integer)
# •	Input a positive integer and check if it’s a palindrome (same forwards and backwards).
# n = input("Enter a positive integer: ")
# if n == n[::-1]:
#     print(f"{n} is a palindrome.")
# else:
#     print(f"{n} is not a palindrome.")
