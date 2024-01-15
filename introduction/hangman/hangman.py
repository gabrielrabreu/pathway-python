import random


def get_random_word():
    return random.choice(["apple", "banana", "cherry", "orange", "grape", "strawberry", "watermelon", "kiwi"])


def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display


def run_game():
    word = get_random_word()
    guessed_letters = []
    max_attempts = 6
    attempts = 0

    print("*********************************")
    print("***Welcome to the Hangman!***")
    print("*********************************")

    while True:
        print("\n" + display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!")
        else:
            print("Incorrect guess.")
            attempts += 1

        if "_" not in display_word(word, guessed_letters):
            print("\nCongratulations! You've guessed the word: " + word)
            break

        if attempts >= max_attempts:
            print("\nYou've run out of attempts. The word was: " + word)
            break
