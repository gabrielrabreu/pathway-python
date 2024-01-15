import random

# Function to get a random word from a predefined list
def get_random_word():
    return random.choice(["apple", "banana", "cherry", "orange", "grape", "strawberry", "watermelon", "kiwi"])

# Function to display the word with guessed letters
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

# Function to run the Hangman game
def run_game():
    word = get_random_word()  # Get a random word
    guessed_letters = []      # List to store guessed letters
    max_attempts = 6         # Maximum allowed attempts
    attempts = 0             # Number of attempts made

    print("*********************************")
    print("*** Welcome to Hangman! ***")
    print("*********************************")

    while True:
        print("\n" + display_word(word, guessed_letters))  # Display the word with guessed letters
        guess = input("Guess a letter: ").lower()            # Get user input and convert to lowercase

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")      # Check for valid input
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")         # Check if letter has already been guessed
            continue

        guessed_letters.append(guess)                          # Add the guessed letter to the list

        if guess in word:
            print("Good guess!")                               # Check if guessed letter is in the word
        else:
            print("Incorrect guess.")
            attempts += 1                                     # Increment the attempts counter for incorrect guesses

        if "_" not in display_word(word, guessed_letters):
            print("\nCongratulations! You've guessed the word: " + word)
            break

        if attempts >= max_attempts:
            print("\nYou've run out of attempts. The word was: " + word)
            break

# Run the Hangman game
if __name__ == "__main__":
    run_game()
