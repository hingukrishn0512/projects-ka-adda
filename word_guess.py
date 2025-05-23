import random
# List of words
l1 = ["krishn", "hingu", "dhaneshbhai", "yash", "pintu", "rinku", "ashishkumar"]

# Randomly pick a word from l1
guess_random = random.choice(l1)

# Ask the user to guess
user_input = input("Guess the word from (krishn, hingu, dhaneshbhai, yash, pintu, rinku, ashishkumar): ")

# Check if the guess is correct
if user_input == guess_random:
    print("You guessed it right! 🎉")
else:
    print(f"Oops! The correct word was '{guess_random}'.")

print("Hope you enjoyed the game!")
