import random

emojis = {'r': '🥌', 's': '✂', 'p': '📃'}
choices = ('r', 'p', 's')


def get_result(player1, player2):
    if player1 == player2:
        return 'tie'
    elif (
        (player1 == 'r' and player2 == 's') or
        (player1 == 's' and player2 == 'p') or
        (player1 == 'p' and player2 == 'r')
    ):
        return 'player1'
    else:
        return 'player2'


def play_round(player1_name, player2_name, is_computer=False):
    while True:
        player1_choice = input(f"{player1_name}, choose (r/p/s): ").lower()
        if player1_choice not in choices:
            print("Invalid choice!")
            continue
        break

    if is_computer:
        player2_choice = random.choice(choices)
    else:
        while True:
            player2_choice = input(f"{player2_name}, choose (r/p/s): ").lower()
            if player2_choice not in choices:
                print("Invalid choice!")
                continue
            break

    print(f"{player1_name} chose {emojis[player1_choice]}")
    print(f"{player2_name} chose {emojis[player2_choice]}")

    result = get_result(player1_choice, player2_choice)

    if result == 'tie':
        print("It's a tie!")
    elif result == 'player1':
        print(f"{player1_name} wins this round!")
    else:
        print(f"{player2_name} wins this round!")

    return result


def game():
    print("Welcome to Rock, Paper, Scissors!")
    mode = input(
        "Choose mode: (1) Single Player vs Computer, (2) Two Player: ").strip()
    single_player = mode == '1'

    if single_player:
        player1_name = "You"
        player2_name = "Computer"
        is_computer = True
    else:
        player1_name = input("Enter Player 1 name: ")
        player2_name = input("Enter Player 2 name: ")
        is_computer = False

    stats = {'wins': 0, 'losses': 0, 'ties': 0}

    while True:
        score = {player1_name: 0, player2_name: 0}
        while score[player1_name] < 2 and score[player2_name] < 2:
            result = play_round(player1_name, player2_name, is_computer)

            if result == 'tie':
                stats['ties'] += 1
            elif result == 'player1':
                score[player1_name] += 1
                if single_player:
                    stats['wins'] += 1
            else:
                score[player2_name] += 1
                if single_player:
                    stats['losses'] += 1

        print(
            f"\n🏆 {player1_name if score[player1_name] == 2 else player2_name} wins the game!\n")

        if single_player:
            print(f"--- Stats ---")
            print(f"Wins: {stats['wins']}")
            print(f"Losses: {stats['losses']}")
            print(f"Ties: {stats['ties']}")

        cont = input("Play another game? (y/n): ").lower()
        if cont != 'y':
            print("Thanks for playing!")
            break


game()
