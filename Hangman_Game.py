import random
import os

word_list = ["mango", "apple", "parrot", "keyword","great","car"]
lives = 6
Chosen_word = random.choice(word_list)
display = ["_"] * len(Chosen_word)

game_over = False

while not game_over:
    # Clear the screen before showing the latest state
    os.system('cls' if os.name == 'nt' else 'clear')

    print("Word to guess: ", " ".join(display))
    print(f"Lives left: {lives}")

    guessed_letter = input("Guess a letter: ").lower()

    for position in range(len(Chosen_word)):
        letter = Chosen_word[position]
        if letter == guessed_letter:
            display[position] = guessed_letter

    if guessed_letter not in Chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            os.system('cls' if os.name == 'nt' else 'clear')
            print("You lose!! The word was:", Chosen_word)

    if '_' not in display:
        game_over = True
        os.system('cls' if os.name == 'nt' else 'clear')
        print("You Win! The word was:", Chosen_word)
