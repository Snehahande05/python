# 71. Write to File
text = input("Enter a string to write to the file: ")
with open("output.txt", "w") as file:
    file.write(text)
print("Text written to 'output.txt'.")

# 72. Read from File
try:
    with open("output.txt", "r") as file:
        content = file.read()
    print("Content of 'output.txt':")
    print(content)
except FileNotFoundError:
    print("'output.txt' not found.")

# 73. Copy File
source = input("Enter the source file name: ")
destination = input("Enter the destination file name: ")
try:
    with open(source, "r") as src, open(destination, "w") as dest:
        dest.write(src.read())
    print(f"Contents of '{source}' copied to '{destination}'.")
except FileNotFoundError:
    print(f"'{source}' not found.")

# 74. Count Lines in a File
filename = input("Enter the file name: ")
try:
    with open(filename, "r") as file:
        lines = file.readlines()
    print(f"Total Lines: {len(lines)}")
except FileNotFoundError:
    print(f"'{filename}' not found.")

# 75. Count Words in a File
filename = input("Enter the file name: ")
try:
    with open(filename, "r") as file:
        words = file.read().split()
    print(f"Total Words: {len(words)}")
except FileNotFoundError:
    print(f"'{filename}' not found.")

# 76. Find Longest Line in a File
filename = input("Enter the file name: ")
try:
    with open(filename, "r") as file:
        lines = file.readlines()
    longest_line = max(lines, key=len, default="")
    print("Longest Line:")
    print(longest_line.strip())
except FileNotFoundError:
    print(f"'{filename}' not found.")

# 77. Search for a Word in a File
filename = input("Enter the file name: ")
word = input("Enter the word to search for: ")
try:
    with open(filename, "r") as file:
        lines = file.readlines()
    line_numbers = [i + 1 for i, line in enumerate(lines) if word in line]
    if line_numbers:
        print(f"'{word}' found on line(s): {line_numbers}")
    else:
        print(f"'{word}' not found in the file.")
except FileNotFoundError:
    print(f"'{filename}' not found.")

# 78. Append to a File
text = input("Enter text to append to 'output.txt': ")
with open("output.txt", "a") as file:
    file.write("\n" + text)
print("Text appended to 'output.txt'.")

# 79. Remove Blank Lines
source = input("Enter the source file name: ")
destination = input("Enter the destination file name: ")
try:
    with open(source, "r") as src, open(destination, "w") as dest:
        for line in src:
            if line.strip():
                dest.write(line)
    print(f"Blank lines removed. Content written to '{destination}'.")
except FileNotFoundError:
    print(f"'{source}' not found.")

# 80. File Statistics
filename = input("Enter the file name: ")
try:
    with open(filename, "r") as file:
        content = file.read()
        lines = content.splitlines()
        words = content.split()
        total_characters = len(content)
        total_lines = len(lines)
        total_words = len(words)
    print("File Statistics:")
    print(f"Total Characters: {total_characters}")
    print(f"Total Lines: {total_lines}")
    print(f"Total Words: {total_words}")
except FileNotFoundError:
    print(f"'{filename}' not found.")
