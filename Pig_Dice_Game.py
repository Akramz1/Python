import random


def player_system(total_players, reqtarget):
    players_score = [0] * total_players
    current_player = 0
    print("-----Game Started-----")
    while True:
        print(f"Player {current_player+1}'s turn")
        score = 0
        double_six = False
        while True:
            die_roll = random.randint(1, 6)
            if die_roll == 6:
                if double_six:
                    print(f"Player {current_player+1} rolled a {die_roll}")
                    print("You rolled double six in a row! you lose all your points.")
                    players_score[current_player] = 0
                    score = 0
                    break
                else:
                    double_six = True
            else:
                double_six = False

            print(f"Player {current_player+1} rolled a {die_roll}")
            if die_roll == 1:
                print("-----------\nYou rolled a 1 :'("
                      "\nYou losing all your points.\n-----------"
                      )
                score = 0
                break

            score += die_roll
            if players_score[current_player] + score >= reqtarget:
                players_score[current_player] += score
                print(
                    f"-----------\nPlayer {current_player+1} reached the target and won with {players_score[current_player]} points!"
                )
                return current_player+1
            while True:
                try:
                    choice = input("Roll again? (y/n): ").lower()
                    if choice not in ('y', 'n'):
                        raise ValueError()
                    break
                except ValueError:
                    print("Enter 'y' or 'n' only")
            if choice != 'y':
                players_score[current_player] += score
                print(
                    f"Player {current_player+1} scored {players_score[current_player]} points this turn.\n-----------"
                )
                break
        for i in range(total_players):
            print(f"Player {i+1}: {players_score[i]}")
        print("-----------")
        current_player = (current_player+1) % total_players


def main():
    print("Welcome to Pig Dice Game!")

    while True:
        try:
            target = int(input("Enter your target(Target must be above 0): "))
            if target <= 0:
                raise ValueError()
            break
        except ValueError:
            print("Enter a number above 0")

    while True:
        try:
            num_of_players = int(input("Enter number of players: "))
            if not (2 <= num_of_players <= 4):
                raise ValueError()
            break
        except ValueError:
            print("Enter a number between 2-4")

    winner = player_system(num_of_players, target)
    print(f"Player {winner} Won the match!")


if __name__ == "__main__":
    main()
