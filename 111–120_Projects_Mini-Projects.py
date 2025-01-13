# 111. Simple Password Generator
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# 112. Contact Book
import json

def add_contact(contact_file, name, number, email):
    try:
        with open(contact_file, 'r') as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = {}
    contacts[name] = {'number': number, 'email': email}
    with open(contact_file, 'w') as file:
        json.dump(contacts, file)
    print("Contact saved!")

def search_contact(contact_file, name):
    try:
        with open(contact_file, 'r') as file:
            contacts = json.load(file)
        if name in contacts:
            print(f"Name: {name}, Number: {contacts[name]['number']}, Email: {contacts[name]['email']}")
        else:
            print("Contact not found.")
    except FileNotFoundError:
        print("Contact file not found.")

# 113. Quiz Game
def quiz_game(questions):
    score = 0
    for question, options, correct in questions:
        print(question)
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        answer = int(input("Enter your choice: "))
        if options[answer - 1] == correct:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
    print(f"Your score: {score}/{len(questions)}")

# 114. Hangman Game
def hangman(word):
    word = word.lower()
    guessed = set()
    attempts = 6
    while attempts > 0 and set(word) - guessed:
        print("Guessed so far:", ''.join(c if c in guessed else '_' for c in word))
        guess = input("Guess a letter: ").lower()
        if guess in guessed:
            print("Already guessed that letter.")
        elif guess in word:
            guessed.add(guess)
            print("Correct!")
        else:
            attempts -= 1
            print(f"Wrong! {attempts} attempts left.")
    if set(word) - guessed:
        print(f"You lost! The word was: {word}")
    else:
        print(f"Congratulations! You guessed the word: {word}")

# 115. Tic-Tac-Toe
def tic_tac_toe():
    board = [' '] * 9
    def print_board():
        for i in range(0, 9, 3):
            print('|'.join(board[i:i+3]))
            if i < 6:
                print('-+-+-')

    def check_winner(player):
        win_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                            (0, 3, 6), (1, 4, 7), (2, 5, 8),
                            (0, 4, 8), (2, 4, 6)]
        return any(all(board[pos] == player for pos in combo) for combo in win_combinations)

    for turn in range(9):
        print_board()
        player = 'X' if turn % 2 == 0 else 'O'
        move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
        if board[move] == ' ':
            board[move] = player
            if check_winner(player):
                print_board()
                print(f"Player {player} wins!")
                return
        else:
            print("Invalid move, try again.")
    print_board()
    print("It's a draw!")

# 116. Text-based Adventure
def text_adventure():
    print("Welcome to the adventure!")
    print("You are in a dark room. You can go 'left' or 'right'.")
    choice = input("What do you do? ").lower()
    if choice == "left":
        print("You encounter a dragon! Game over.")
    elif choice == "right":
        print("You find a treasure chest! You win!")
    else:
        print("Invalid choice. Game over.")

# 117. Rock-Paper-Scissors
def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    user = input("Enter your choice (rock/paper/scissors): ").lower()
    computer = random.choice(choices)
    print(f"Computer chose: {computer}")
    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You win!")
    else:
        print("You lose!")

# 118. Email Slicer
def email_slicer(email):
    username, domain = email.split('@')
    print(f"Username: {username}, Domain: {domain}")

# 119. Dictionary App
def dictionary_app(word, dictionary):
    print(dictionary.get(word.lower(), "Word not found."))

# 120. Basic To-Do List Manager
def to_do_list():
    tasks = []
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Mark Task as Done\n4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            task = input("Enter a new task: ")
            tasks.append({"task": task, "done": False})
        elif choice == "2":
            for i, t in enumerate(tasks, 1):
                status = "Done" if t["done"] else "Pending"
                print(f"{i}. {t['task']} [{status}]")
        elif choice == "3":
            task_num = int(input("Enter task number to mark as done: "))
            if 1 <= task_num <= len(tasks):
                tasks[task_num - 1]["done"] = True
            else:
                print("Invalid task number.")
        elif choice == "4":
            break
        else:
            print("Invalid option.")
