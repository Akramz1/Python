import random


def play_game():
    print("Welcome to the guessing game! You can decide the number of attempts to guess the number, Good luck!")
    while True:
        try:
            mini = int(input("Choose the minimum number to be guessed: "))
            mx = int(input("Choose the max number to be guessed: "))
            if mx <= mini:
                print("Maximum must be greater than minimum. Try again.")
                continue
            break
        except ValueError:
            print("Please enter valid integers.")
    rnumber = random.randint(mini, mx)  # the number to be guessed
    difficulty = input(
        "Enter the difficulty you wish to play (easy,medium,hard): ")
    rounds = 0
    attempts = 0
    if difficulty == "easy":
        rounds = 10
        print("You have 10 Attempts!")
    elif difficulty == "medium":
        rounds = 7
        print("You have 7 Attempts! Pay attention to your moves")
    elif difficulty == "hard":
        rounds = 5
        print("You have 5 Attempts! You must be that good huh")
    while attempts < rounds:
        try:
            num = int(input(f"Guess the number between {mini} to {mx}: "))
            if num == rnumber:
                attempts += 1
                print(
                    f"Congratulation! You guessed the number in {attempts} tries.")
                return attempts
            elif num > rnumber and num <= mx:
                attempts += 1
                print("Too high!")
            elif num < rnumber and num >= mini:
                attempts += 1
                print("Too low!")
            else:
                print(f"Enter a valid number between {mini} and {mx}.")
        except ValueError:
            print("Please enter a valid number")

    print(f"Game over! The number was {rnumber}.")


best_score = None

while True:
    current_score = int(play_game())

    if best_score is None or current_score < best_score:
        best_score = current_score

    print(f"Your best score: {best_score} attempts")

    while True:
        replay = input("Play again? (y/n): ").strip().lower()
        if replay in ['y', 'n']:
            break
        print("Invalid input. Please enter 'y' or 'n'.")
    if replay == 'n':
        print("Thanks for playing!")
        break
