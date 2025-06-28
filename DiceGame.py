import random
counter = 0
while True:
    choice = input("Roll the dice? (y/n):")
    if choice == 'n':
        print("Thanks for playing!")
        break
    elif choice == 'y':
        num = int(input("How many dice would you like to roll? (1 or 2?)"))
        if num == 2:
            counter += 2
            print(
                f"({random.randint(1, 6)}, {random.randint(1, 6)}) Number of dice you rolled: {counter}")
        else:
            counter += 1
            print(f"{random.randint(1, 6)} Number of dice you rolled: {counter}")
    else:
        print("Invalid Choice")
