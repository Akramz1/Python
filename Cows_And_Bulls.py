import random


def input_from_user():
    while True:
        try:
            guess = input("Guess: ")
            if len(guess) != 4 or not guess.isdigit() or '0' in guess:
                raise ValueError("Enter 4 unique digits")
            return guess
        except ValueError:
            print("Enter 4 unique digits thats contains numbers from 1 to 9")


def generate_the_answer():
    digits = random.sample('123456789', 4)
    return ''.join(digits)


def game(right_answer, attempt):
    print(
        f"I have generated a 4-digit number with unique digits. Try to guess it in {attempt} tries!")
    count = 0
    hint_given = 0

    while count < attempt:
        cows = 0
        bulls = 0
        guess = input_from_user()
        count += 1

        if hint_given < 2 and count >= (attempt * (hint_given+1)/3):
            print(
                f"\nHint {hint_given + 1}: The digit {right_answer[hint_given]} is in the answer 😉")
            hint_given += 1
        for i in range(4):
            if guess[i] == right_answer[i]:
                bulls += 1
            elif guess[i] in right_answer:
                cows += 1

        print(f"{cows} Cows, {bulls} Bulls")
        if bulls == 4:
            print(
                f"Congratulations! 🏆 You guessed {right_answer} in {count} tries!"
            )
            return
    print(
        f"\nGame over! The number was {right_answer}. Better luck next time!")


def main():
    print("Welcome to Cows and Bulls")
    while True:
        while True:
            try:
                attempts = int(input("Enter number of attempts (5-20): "))
                if 5 <= attempts <= 20:
                    break
                print("Enter a number between 5 and 20")
            except ValueError:
                print("Enter a number")
        answer = generate_the_answer()
        game(answer, attempts)
        if input("\nPlay again? (y/n): ").lower() != 'y':
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
