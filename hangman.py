import random

def get_random_word():
    # List of words to choose from
    words = ['python', 'hangman', 'challenge', 'code', 'programming', 'random', 'visual']
    return random.choice(words)

def display_current_state(word, guessed_letters):
    display_word = [letter if letter in guessed_letters else '_' for letter in word]
    return ' '.join(display_word)

def hangman_game():
    word_to_guess = get_random_word()
    guessed_letters = []
    wrong_guesses = 0
    max_wrong_guesses = 6
    game_over = False
    
    print("Welcome to Hangman!")
    print(f"You have {max_wrong_guesses} incorrect guesses allowed.")
    
    while not game_over:
        print(f"\nCurrent word: {display_current_state(word_to_guess, guessed_letters)}")
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue
        
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
            continue
        
        guessed_letters.append(guess)
        
        if guess in word_to_guess:
            print(f"Good job! '{guess}' is in the word.")
        else:
            wrong_guesses += 1
            print(f"Oops! '{guess}' is not in the word. You have {max_wrong_guesses - wrong_guesses} guesses left.")
        
        if wrong_guesses >= max_wrong_guesses:
            game_over = True
            print(f"\nYou lost! The correct word was '{word_to_guess}'.")
        
        if all(letter in guessed_letters for letter in word_to_guess):
            game_over = True
            print(f"\nCongratulations! You've guessed the word '{word_to_guess}' correctly!")

if __name__ == "__main__":
    hangman_game()
p