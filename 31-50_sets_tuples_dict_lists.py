# 31. List Operations
lst = [1, 2, 3]
print("Initial List:", lst)
lst.append(4)
print("After Append:", lst)
lst.insert(2, 5)
print("After Insert at index 2:", lst)
lst.remove(3)
print("After Remove 3:", lst)
lst.pop()
print("After Pop:", lst)

# 32. Maximum and Minimum in a Tuple
tpl = ("apple", "banana", "cherry", "date")
index = int(input("Enter an index: "))
if 0 <= index < len(tpl):
    print("Element at index", index, ":", tpl[index])
else:
    print("Invalid index!")

# 33. Second Largest Element
nums = [5, 2, 9, 1, 6]
nums.sort()
print("Second Largest Element:", nums[-2])

# 34. Sum and Average of a List
nums = list(map(int, input("Enter numbers separated by space: ").split()))
print("Sum:", sum(nums))
print("Average:", sum(nums) / len(nums))

# 35. Count Positive, Negative, Zero
nums = list(map(int, input("Enter numbers separated by space: ").split()))
pos, neg, zero = 0, 0, 0
for num in nums:
    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1
    else:
        zero += 1
print(f"Positive: {pos}, Negative: {neg}, Zero: {zero}")

# 36. Remove Duplicates from a List
nums = list(map(int, input("Enter numbers separated by space: ").split()))
unique_nums = list(set(nums))
print("List with Duplicates Removed:", unique_nums)

# 37. Concatenate Two Lists
list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))
print("Concatenated List:", list1 + list2)

# 38. List Reversal
lst = list(map(int, input("Enter a list: ").split()))
lst.reverse()
print("Reversed List:", lst)

# 39. Find Common Elements of Two Lists
list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))
common = list(set(list1) & set(list2))
print("Common Elements:", common)

# 40. Element-wise Sum of Two Lists
list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))
if len(list1) == len(list2):
    sum_list = [a + b for a, b in zip(list1, list2)]
    print("Element-wise Sum:", sum_list)
else:
    print("Lists must be of equal length!")

# 41. Tuple Creation and Access
tpl = ("apple", "banana", "cherry", "date")
index = int(input("Enter an index: "))
if 0 <= index < len(tpl):
    print("Element at index", index, ":", tpl[index])
else:
    print("Invalid index!")

# 42. Tuple to List
tpl = tuple(map(int, input("Enter elements of the tuple separated by space: ").split()))
lst = list(tpl)
print("List:", lst)
lst.append(100)  # Modify the list
tpl = tuple(lst)
print("Modified Tuple:", tpl)

# 43. Check if Element Exists in Tuple
tpl = tuple(map(int, input("Enter elements of the tuple separated by space: ").split()))
element = int(input("Enter an element to check: "))
print("Exists in Tuple:", element in tpl)

# 44. Dictionary: Word Count
sentence = input("Enter a sentence: ")
words = sentence.split()
word_count = {word: words.count(word) for word in set(words)}
print("Word Count:", word_count)

# 45. Dictionary: Student Grades
grades = {"Alice": 85, "Bob": 90, "Charlie": 78}
name = input("Enter student name: ")
print("Grade:", grades.get(name, "Student not found"))

# 46. Dictionary: Keys and Values
d = {"a": 1, "b": 2, "c": 3}
print("Keys:", list(d.keys()))
print("Values:", list(d.values()))

# 47. Merge Two Dictionaries
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
merged_dict = {**d1, **d2}
print("Merged Dictionary:", merged_dict)

# 48. Invert Dictionary
d = {"a": 1, "b": 2, "c": 3}
if len(d) == len(set(d.values())):
    inverted = {v: k for k, v in d.items()}
    print("Inverted Dictionary:", inverted)
else:
    print("Cannot invert, values are not unique!")

# 49. Set Operations
list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))
set1, set2 = set(list1), set(list2)
print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)

# 50. Set Membership Testing
names = {"Alice", "Bob", "Charlie"}
name = input("Enter a name: ")
print("Exists in Set:", name in names)
