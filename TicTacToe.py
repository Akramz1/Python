def create_board():
    board = []
    for i in range(0, 7):
        line = ""
        if i == 0 or i == 2 or i == 4 or i == 6:
            for j in range(1, 12):
                if j % 4 == 0 and j != 0:
                    line += "+"
                else:
                    line += "-"
        else:
            for j in range(1, 12):
                if j % 4 == 0:
                    line += "|"
                else:
                    line += " "
        board.append(line)
    return board


def print_board(board):
    for line in board:
        print(line)


def is_draw(board):
    for r in [1, 3, 5]:
        for c in [1, 5, 9]:
            if board[r][c] == " ":
                return False
    return True


O_Score = 0
X_Score = 0
game = create_board()
player_turn = 0

while True:
    print_board(game)
    print("Player O's turn" if player_turn % 2 == 0 else "Player X's turn")

    while True:
        row = int(input("Enter row (0-2): "))
        column = int(input("Enter column (0-2): "))

        game_row = 1 if row == 0 else 3 if row == 1 else 5
        game_col = 1 if column == 0 else 5 if column == 1 else 9

        if game[game_row][game_col] != " ":
            print("Cell is already taken. Try again.\n")
        else:
            break

    x_o = "O" if player_turn % 2 == 0 else "X"

    game_line = list(game[game_row])
    game_line[game_col] = x_o
    game[game_row] = "".join(game_line)

    player_turn += 1

    win_lines = [
        # Rows
        [(1, 1), (1, 5), (1, 9)],
        [(3, 1), (3, 5), (3, 9)],
        [(5, 1), (5, 5), (5, 9)],
        # Columns
        [(1, 1), (3, 1), (5, 1)],
        [(1, 5), (3, 5), (5, 5)],
        [(1, 9), (3, 9), (5, 9)],
        # Diagonals
        [(1, 1), (3, 5), (5, 9)],
        [(1, 9), (3, 5), (5, 1)],
    ]

    for line in win_lines:
        if all(game[r][c] == x_o for r, c in line):
            print_board(game)
            print(f"Player {x_o} won!")
            if x_o == 'O':
                O_Score += 1
            else:
                X_Score += 1
            play_again = input("Play again? (y/n): ").lower()
            if play_again == "y":
                game = create_board()
                player_turn = 0
                break  # restart game loop
            else:
                print(
                    f"-------------------\nPlayer O's score: {O_Score}\nPlayer X's score: {X_Score}"
                )
                exit()

    else:  # no break from the for loop means no winner yet
        if is_draw(game):
            print_board(game)
            print("It's a draw!")
            play_again = input("Play again? (y/n): ").lower()
            if play_again == "y":
                game = create_board()
                player_turn = 0
            else:
                print(
                    f"-------------------\nPlayer O's score: {O_Score}\nPlayer X's score: {X_Score}"
                )
                exit()
