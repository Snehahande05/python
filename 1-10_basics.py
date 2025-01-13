# 1.	Print “Hello, World!”
# •	A classic first program. Just print the string "Hello, World!".
print("Hello, World!" )


# 2.	Variables and Data Types
# •	Prompt the user for their name and age. Print them in a sentence 
# (e.g., "Your name is ... and your age is ...").
name = input("Enter your name:")
age = input("Enter your age :")
print(f"your name is {name} and your age is {age}")


# 3.	Arithmetic Operations
# •	Prompt for two numbers. 
# Compute and display the sum, difference, product, division, and modulus of those two numbers.
num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
print(f"Sum :{num1 + num2}")
print(f"Difference: {num1 - num2}")
print(f"Product: {num1 * num2}")
print(f"Division: {num1 / num2}")
print(f"Modulus: {num1 % num2}")


# 4.	Convert Celsius to Fahrenheit
# •	Take a temperature in Celsius (input from the user) and convert it to Fahrenheit.
Celsius = float(input("Enter the celsius temp:"))
fahrenheit= (Celsius * 9/5) + 32
print(f"The temperature in Fahrenheit is: {fahrenheit} .")


# 5.	Swap Two Variables
# •	Prompt for two variables and swap their values. 
# Show the results before and after swapping.
var1 = input("Enter the first variable:")
var2 = input("Enter the second variable:")
print(f"Before swapping var1:{var1} , var2 : {var2}")
var1 , var2 = var2 , var1
print(f"After swapping var1:{var1},var2:{var2}")


# 6.	Even or Odd
# •	Ask the user for a number and determine if it is even or odd.
num = int(input("Enter the number:"))
if num % 2 == 0:
    print("number is even")
else:
    print("number is odd")


# 7.	Check Vowel or Consonant
# •	Input a letter from the user and check if it’s a vowel or a consonant.
letter = input("Enter the letter:").lower()
if letter in ("aeiou"):
    print("The letter is vowel")
else:
    print("The letter is consonant")


# 8.	Square, Cube, and Square Root
# Input a number and display its square, cube, and square root.
num = int(input("Enter the number:"))
print(f"Square: {num ** 2}")
print(f"Cube : {num ** 3}")
print(f"Square root: {num ** 0.5}")


# 9. Area of Circle
# •	Input the radius of a circle and compute its area. Use π = 3.14159.
radius = float(input("Enter the radius of circle:"))
pi = 3.14159
area = pi * radius * 2
print(f"The area of circle is : {area}")


# 10.	**Simple Interest Calculation**
# •	Input principal, rate, and time. Compute the simple interest as SI = (principal * rate * time) 
Principal = int(input("Enter the principal amount:"))
Rate = int(input("Enter the rate of interest in % :"))/100
Time = int(input("Enter the time in years :"))
simple_interest = Principal * Rate * Time
print(f"The Simple Interest is calculated as:{simple_interest}")
