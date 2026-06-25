import random
def play_hangman():
    # Predefined high-status, sharp words for the pool
    word_pool = ["EMPIRE", "VISION", "LEADER", "MATRIX", "CRUX"]

    # Select a random word and convert it to uppercase
    secret_word = random.choice(word_pool).upper()

    # Track guessed letters
    guessed_letters = set()

    # Game configuration
    incorrect_guesses_left = 6

    print("=== WELCOME TO HANGMAN ===")
    print(f"The mystery word has {len(secret_word)} letters.")

    # Main game loop
    while incorrect_guesses_left > 0:
        print("\n" + "-" * 30)

        # Display the current state of the word (e.g., L _ _ D _ R)
        display_word = [
            letter if letter in guessed_letters else "_" for letter in secret_word
        ]
        print(f"Word: {' '.join(display_word)}")
        print(f"Incorrect guesses remaining: {incorrect_guesses_left}")
        print(
            f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}"
        )

        # Get and validate player input
        guess = input("Guess a letter: ").strip().upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single alphabetical letter.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
            continue

        # Process the valid guess
        guessed_letters.add(guess)

        if guess in secret_word:
            print(f"Sharp! '{guess}' is in the word.")
            # Check for win condition
            if all(letter in guessed_letters for letter in secret_word):
                print("\n==============================")
                print(
                    f"CONGRATULATIONS! You won. The word was: {secret_word}"
                )
                print("==============================")
                break
        else:
            print(f"Incorrect. '{guess}' is not in the word.")
            incorrect_guesses_left -= 1

    # Check for lose condition
    if incorrect_guesses_left == 0:
        print("\n==============================")
        print(f"GAME OVER. You've run out of guesses.")
        print(f"The correct word was: {secret_word}")
        print("==============================")


if __name__ == "__main__":
    play_hangman()
