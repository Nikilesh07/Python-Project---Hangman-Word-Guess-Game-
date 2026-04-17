import random

print("🎯 Welcome to Word Guess Game!")

# word list
word_list = ["python", "cyber", "security", "network", "hacker", "coding"]

# select random word
secret_word = random.choice(word_list)

guessed = []
attempts = 6

# function to show word
def show_word():
    result = ""
    for ch in secret_word:
        if ch in guessed:
            result += ch + " "
        else:
            result += "_ "
    return result

# game loop
while attempts > 0:
    print("\nWord:", show_word())
    print("Remaining Attempts:", attempts)

    user_input = input("Guess a letter: ").lower()

    # validation
    if len(user_input) != 1 or not user_input.isalpha():
        print("❌ Please enter a single alphabet only!")
        continue

    if user_input in guessed:
        print("⚠ Already guessed!")
        continue

    guessed.append(user_input)

    if user_input in secret_word:
        print("✅ Good guess!")
    else:
        print("❌ Incorrect!")
        attempts -= 1

    # win condition
    if all(letter in guessed for letter in secret_word):
        print("\n🎉 Congratulations! You guessed the word:", secret_word)
        break

# lose condition
if attempts == 0:
    print("\n💀 Game Over!")
    print("Correct word was:", secret_word)

