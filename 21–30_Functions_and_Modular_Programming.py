# 21.	Create a Simple Calculator (Functions)
# •	Write four functions: add(a, b), subtract(a, b), multiply(a, b), and divide(a, b). 
# Then prompt the user for two numbers and the operation. 
# Use the corresponding function to output the result.
# def add(a, b): return a + b
# def subtract(a, b): return a - b
# def multiply(a, b): return a * b
# def divide(a, b): return a / b if b != 0 else "Cannot divide by zero"

# a, b = map(float, input("Enter two numbers separated by space: ").split())
# operation = input("Choose operation (+, -, *, /): ")
# print({
#     '+': add(a, b),
#     '-': subtract(a, b),
#     '*': multiply(a, b),
#     '/': divide(a, b)
# }.get(operation, "Invalid operation"))

# 22.	Power Function
# •	Write a function power(base, exponent) that returns base^exponent without using the built-in ** operator (use a loop).
# def power(base, exponent):
#     result = 1
#     for _ in range(exponent):
#         result *= base
#     return result

# base, exp = map(int, input("Enter base and exponent: ").split())
# print(f"{base}^{exp} = {power(base, exp)}")

# 23.	Count Characters in a String (Function)
# •	Write a function that accepts a string and returns the number of characters in it.
# def count_characters(string): return len(string)

# s = input("Enter a string: ")
# print(f"Number of characters: {count_characters(s)}")

# 24.	Check Prime (Function)
# •	Write a function is_prime(n) to check if a number n is prime. Test it with user input.
# def is_prime(n):
#     if n < 2: return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0: return False
#     return True

# n = int(input("Enter a number: "))
# print(f"{n} is {'prime' if is_prime(n) else 'not prime'}.")

# 25.	Fibonacci Series (Function)
# •	Write a function fibonacci(n) that returns a list of the first n Fibonacci numbers.
# def fibonacci(n):
#     fib = [0, 1]
#     for i in range(2, n): fib.append(fib[-1] + fib[-2])
#     return fib[:n]

# n = int(input("Enter the number of Fibonacci terms: "))
# print(f"Fibonacci series: {fibonacci(n)}")

# 26.	GCD of Two Numbers
# •	Write a function gcd(a, b) that computes the greatest common divisor of a and b.
# def gcd(a, b):
#     while b: a, b = b, a % b
#     return a

# a, b = map(int, input("Enter two numbers: ").split())
# print(f"GCD of {a} and {b} is {gcd(a, b)}")

# 27.	LCM of Two Numbers
# •	Write a function lcm(a, b) that finds the least common multiple of a and b. 
# Hint: lcm(a, b) = abs(a*b)/gcd(a,b).
# def gcd(a, b): return b and gcd(b, a % b) or a
# def lcm(a, b): return abs(a * b) // gcd(a, b)

# a, b = map(int, input("Enter two numbers: ").split())
# print(f"LCM of {a} and {b} is {lcm(a, b)}")

# 28.	Factorial (Recursive)
# •	Write a recursive function to compute the factorial of a number.
# def factorial(n): return 1 if n == 0 else n * factorial(n - 1)

# n = int(input("Enter a number: "))
# print(f"Factorial of {n} is {factorial(n)}")

# 29.	Tower of Hanoi
# •	Write a recursive function to solve the Tower of Hanoi puzzle for n disks.
# def tower_of_hanoi(n, source, target, auxiliary):
#     if n == 1:
#         print(f"Move disk 1 from {source} to {target}")
#         return
#     tower_of_hanoi(n - 1, source, auxiliary, target)
#     print(f"Move disk {n} from {source} to {target}")
#     tower_of_hanoi(n - 1, auxiliary, target, source)

# n = int(input("Enter number of disks: "))
# tower_of_hanoi(n, 'A', 'C', 'B')

# 30.	Count Occurrences of an Element
# •	Write a function count_occurrences(lst, x) that returns how many times x appears in the list
# def count_occurrences(lst, x): return lst.count(x)

# lst = list(map(int, input("Enter list elements separated by space: ").split()))
# x = int(input("Enter the element to count: "))
# print(f"{x} occurs {count_occurrences(lst, x)} times in the list.")