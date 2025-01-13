# 61. Armstrong Number
num = int(input("Enter a number: "))
order = len(str(num))
sum_of_powers = sum(int(digit) ** order for digit in str(num))
if sum_of_powers == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")

# 62. Strong Number
import math

num = int(input("Enter a number: "))
sum_of_factorials = sum(math.factorial(int(digit)) for digit in str(num))
if sum_of_factorials == num:
    print(f"{num} is a Strong number.")
else:
    print(f"{num} is not a Strong number.")

# 63. Perfect Number
num = int(input("Enter a number: "))
divisors = [i for i in range(1, num) if num % i == 0]
if sum(divisors) == num:
    print(f"{num} is a Perfect number.")
else:
    print(f"{num} is not a Perfect number.")

# 64. Sum of Digits
num = int(input("Enter a number: "))
sum_of_digits = sum(int(digit) for digit in str(num))
print("Sum of Digits:", sum_of_digits)

# 65. Binary to Decimal Conversion
binary = input("Enter a binary number: ")
decimal = int(binary, 2)
print(f"Decimal of {binary}: {decimal}")

# 66. Decimal to Binary Conversion
decimal = int(input("Enter a decimal number: "))
binary = bin(decimal)[2:]
print(f"Binary of {decimal}: {binary}")

# 67. Prime Factors of a Number
def prime_factors(n):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors

num = int(input("Enter a number: "))
print("Prime Factors:", prime_factors(num))

# 68. Number to Words
def number_to_words(num):
    words_map = {
        '0': "zero", '1': "one", '2': "two", '3': "three", '4': "four",
        '5': "five", '6': "six", '7': "seven", '8': "eight", '9': "nine"
    }
    return ' '.join(words_map[digit] for digit in str(num))

num = int(input("Enter a number: "))
print("Number in Words:", number_to_words(num))

# 69. LCM of a Range
from math import gcd

def lcm(a, b):
    return (a * b) // gcd(a, b)

n = int(input("Enter the range (1 to n): "))
result = 1
for i in range(1, n + 1):
    result = lcm(result, i)
print(f"LCM of numbers from 1 to {n}:", result)

# 70. Sieve of Eratosthenes
def sieve_of_eratosthenes(n):
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return [i for i in range(n + 1) if primes[i]]

n = int(input("Enter the range (up to n): "))
print("Prime Numbers:", sieve_of_eratosthenes(n))
