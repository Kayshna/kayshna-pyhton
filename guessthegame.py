#!/usr/bin/env python
import time
import os

def get_difficulty_level():
    #Prompt user to select a difficulty level.
    print("Choose difficulty level:")
    print("1. Easy (5 chances)")
    print("2. Medium (3 chances)")
    print("3. Hard (1 chance)")
    while True:
        choice = input("Enter the number of your choice: ")
        if choice == '1':
            return 5
        elif choice == '2':
            return 3
        elif choice == '3':
            return 1
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def print_header():
    #to print the game header.
    print("\n" + "*" * 50)
    print("*** WELCOME TO THE GUESSING GAME! ***")
    print("Try to guess the correct game.")
    print("*" * 50 + "\n")

def clear_screen():
    #to clear the screen.
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    #Start of the guessing game.
    correct_game = 'Genshin Impact'
    hints =print (
         "It has gacha mechanics!",
         "This game has some fighting elements.",
         "This game has a lot of characters and is open world.")
    

    while True:
        print_header()
        chances = get_difficulty_level()
        remaining_chances = chances
        score = 0
        start_time = time.time()

        while remaining_chances > 0:
            guess = input("Guess the game: ").strip()
            if guess.lower() == correct_game.lower():
                elapsed_time = time.time() - start_time
                score = max(0, 100 - int(elapsed_time))  # Score decreases with time
                clear_screen()
                print_header()
                print("Correct! You've guessed the game in ",int(elapsed_time), "seconds.")
                print("Your score is:", score)
                break
            else:1
            remaining_chances -= 1
            clear_screen()
            print_header()
            if remaining_chances > 0:
                    hint = hints.get(remaining_chances, "No more hints.")
                    chance_word = "chances" if remaining_chances > 1 else "chance"
                    print(hint)
                    print("Try again! You have", remaining_chances, chance_word , " left.")
            else:
                    print("Sorry, you're out of chances.")
                    print("The correct game was:",correct_game)
                    print("Your final score is:", score)

        print("\nDo you want to play again? (yes/no)")
        if input().strip().lower() != 'yes':
            print("\n*** Thank you for playing! Have a great day! ***")
            break
        else:
            clear_screen()
            print_header()

if __name__ == "__main__":
    main()
