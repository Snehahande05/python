# 51. Reverse a String
string = input("Enter a string: ")
reversed_string = string[::-1]
print("Reversed String:", reversed_string)

# 52. Palindrome String Checker
string = input("Enter a string: ")
case_insensitive = string.lower()
if case_insensitive == case_insensitive[::-1]:
    print("The string is a palindrome!")
else:
    print("The string is not a palindrome.")

# 53. Count Vowels in a String
string = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in string if char in vowels)
print("Number of Vowels:", vowel_count)

# 54. Check Anagram
string1 = input("Enter the first string: ").replace(" ", "").lower()
string2 = input("Enter the second string: ").replace(" ", "").lower()
if sorted(string1) == sorted(string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")

# 55. Remove Spaces
string = input("Enter a string: ")
no_spaces = string.replace(" ", "")
print("String without Spaces:", no_spaces)

# 56. Longest Word in a Sentence
sentence = input("Enter a sentence: ")
words = sentence.split()
longest_word = max(words, key=len)
print("Longest Word:", longest_word)

# 57. String Case Conversion
string = input("Enter a string: ")
print("Upper Case:", string.upper())
print("Lower Case:", string.lower())
print("Title Case:", string.title())

# 58. Capitalize Every Word
string = input("Enter a string: ")
capitalized = ' '.join(word.capitalize() for word in string.split())
print("Capitalized String:", capitalized)

# 59. Count Special Characters
import string as str_lib

user_input = input("Enter a string: ")
special_characters = set(str_lib.punctuation)
special_count = sum(1 for char in user_input if char in special_characters)
print("Number of Special Characters:", special_count)

# 60. Character Frequency in String
string = input("Enter a string: ")
frequency = {char: string.count(char) for char in set(string)}
print("Character Frequency:", frequency)
