import random

words = ["python", "apple", "chair", "table", "phone", "water", "plant", "mouse", "light", "train"]

word = random.choice(words)

scrambled = ''.join(random.sample(word, len(word)))

print("Guess the word:", scrambled)

attempts = 3

while attempts > 0:
    guess = input("Your guess: ").lower()
    
    if guess == word:
        print("Correct! You win 🎉")
        break
    else:
        attempts -= 1
        print("Wrong! Attempts left:", attempts)

if attempts == 0:
    print("You lost! The correct word was:", word)