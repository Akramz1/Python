

def printa():
    word = ""
    for row in range(7):
        for column in range(6):
            if (row == 0 and (column == 1 or column == 2 or column == 3 or column == 4)) or \
                (row == 1 and (column == 0 or column == 5)) or  \
                (row == 2 and (column == 0 or column == 5)) or\
                (row == 3 and (column == 0 or column == 5)) or \
                (row == 4 and (column == 0 or column == 1 or column == 2 or column == 3 or column == 4 or column == 5)) or \
                (row == 5 and (column == 0 or column == 5)) or \
                    (row == 6 and (column == 0 or column == 5)):
                word += '*'
            else:
                word += " "
        word += "\n"
    return word


def printb():
    word = ""
    for row in range(7):
        for column in range(6):
            if (row == 0 and (column == 0 or column == 1 or column == 2 or column == 3 or column == 4)) or\
               (row == 1 and (column == 0 or column == 5)) or\
               (row == 2 and (column == 0 or column == 5)) or\
               (row == 3 and (column == 0 or column == 1 or column == 2 or column == 3 or column == 4)) or\
               (row == 4 and (column == 0 or column == 5)) or\
               (row == 5 and (column == 0 or column == 5)) or\
               (row == 6 and (column == 0 or column == 1 or column == 2 or column == 3 or column == 4)):
                word += "*"
            else:
                word += " "
        word += "\n"
    return word


def printc():
    word = ""
    for row in range(7):
        for column in range(6):
            if (row == 0 and (column == 0 or column == 1 or column == 2 or column == 3 or column == 4 or column == 5)) or\
               (row == 1 and (column == 0)) or\
               (row == 2 and (column == 0)) or\
               (row == 3 and (column == 0)) or\
               (row == 4 and (column == 0)) or\
               (row == 5 and (column == 0)) or\
               (row == 6 and (column == 0 or column == 1 or column == 2 or column == 3 or column == 4 or column == 5)):
                word += "*"
            else:
                word += " "
        word += "\n"
    return word


def printe():
    word = ""
    for row in range(7):
        for column in range(6):
            if (row == 0 and (column == 0 or column == 1 or column == 2 or column == 3 or column == 4 or column == 5)) or\
               (row == 1 and (column == 0)) or\
               (row == 2 and (column == 0)) or\
               (row == 3 and (column == 0 or column == 1 or column == 2 or column == 3 or column == 4 or column == 5)) or\
               (row == 4 and (column == 0)) or\
               (row == 5 and (column == 0)) or\
               (row == 6 and (column == 0 or column == 1 or column == 2 or column == 3 or column == 4 or column == 5)):
                word += "*"
            else:
                word += " "
        word += "\n"
    return word


def printd():
    word = ""
    for row in range(7):
        for column in range(6):
            if (row == 0 and (column == 0 or column == 1 or column == 2 or column == 3 or column == 4)) or\
               (row == 1 and (column == 0 or column == 5)) or\
               (row == 2 and (column == 0 or column == 5)) or\
               (row == 3 and (column == 0 or column == 5)) or\
               (row == 4 and (column == 0 or column == 5)) or\
               (row == 5 and (column == 0 or column == 5)) or\
               (row == 6 and (column == 0 or column == 1 or column == 2 or column == 3 or column == 4)):
                word += "*"
            else:
                word += " "
        word += "\n"
    return word


def printf():
    word = ""
    for row in range(7):
        for column in range(6):
            if (row == 0 and (column == 0 or column == 1 or column == 2 or column == 3 or column == 4 or column == 5)) or\
               (row == 1 and (column == 0)) or\
               (row == 2 and (column == 0 or column == 1 or column == 2 or column == 3 or column == 4 or column == 5)) or\
               (row == 3 and (column == 0)) or\
               (row == 4 and (column == 0)) or\
               (row == 5 and (column == 0)) or\
               (row == 6 and (column == 0)):
                word += "*"
            else:
                word += " "
        word += "\n"
    return word


def printg():
    word = ""
    for row in range(7):
        for column in range(6):
            if (row == 0 and (column == 0 or column == 1 or column == 2 or column == 3 or column == 4 or column == 5)) or\
               (row == 1 and (column == 0)) or\
               (row == 2 and (column == 0)) or\
               (row == 3 and (column == 0)) or\
               (row == 4 and (column == 0 or column == 3 or column == 4 or column == 5)) or\
               (row == 5 and (column == 0 or column == 5)) or\
               (row == 6 and (column == 0 or column == 1 or column == 2 or column == 3 or column == 4 or column == 5)):
                word += "*"
            else:
                word += " "
        word += "\n"
    return word


def printh():
    word = ""
    for row in range(7):
        for column in range(6):
            if (row == 0 and (column == 0 or column == 5)) or\
               (row == 1 and (column == 0 or column == 5)) or\
               (row == 2 and (column == 0 or column == 5)) or\
               (row == 3 and (column == 0 or column == 1 or column == 2 or column == 3 or column == 4 or column == 5)) or\
               (row == 4 and (column == 0 or column == 5)) or\
               (row == 5 and (column == 0 or column == 5)) or\
               (row == 6 and (column == 0 or column == 5)):
                word += "*"
            else:
                word += " "
        word += "\n"
    return word


def printi():
    word = ""
    for row in range(7):
        for column in range(6):
            if (row == 0 and (column == 0 or column == 1 or column == 2 or column == 3 or column == 4 or column == 5)) or\
               (row == 1 and (column == 2)) or\
               (row == 2 and (column == 2)) or\
               (row == 3 and (column == 2)) or\
               (row == 4 and (column == 2)) or\
               (row == 5 and (column == 2)) or\
               (row == 6 and (column == 0 or column == 1 or column == 2 or column == 3 or column == 4 or column == 5)):
                word += "*"
            else:
                word += " "
        word += "\n"
    return word


def printj():
    word = ""
    for row in range(7):
        for column in range(6):
            if (row == 0 and (column == 2 or column == 3 or column == 4 or column == 5)) or\
               (row == 1 and (column == 5)) or\
               (row == 2 and (column == 5)) or\
               (row == 3 and (column == 5)) or\
               (row == 4 and (column == 5 or column == 0)) or\
               (row == 5 and (column == 5 or column == 0)) or\
               (row == 6 and (column == 0 or column == 1 or column == 2 or column == 3 or column == 4)):
                word += "*"
            else:
                word += " "
        word += "\n"
    return word


def printk():
    word = ""
    for row in range(7):
        for column in range(6):
            if (row == 0 and (column == 0 or column == 5)) or\
               (row == 1 and (column == 0 or column == 4)) or\
               (row == 2 and (column == 0 or column == 3)) or\
               (row == 3 and (column == 0 or column == 1 or column == 2)) or\
               (row == 4 and (column == 0 or column == 3)) or\
               (row == 5 and (column == 0 or column == 4)) or\
               (row == 6 and (column == 0 or column == 5)):
                word += "*"
            else:
                word += " "
        word += "\n"
    return word


def printl():
    word = ""
    for row in range(7):
        for column in range(6):
            if (row == 0 and (column == 0)) or\
               (row == 1 and (column == 0)) or\
               (row == 2 and (column == 0)) or\
               (row == 3 and (column == 0)) or\
               (row == 4 and (column == 0)) or\
               (row == 5 and (column == 0)) or\
               (row == 6 and (column == 0 or column == 1 or column == 2 or column == 3 or column == 4 or column == 5)):
                word += "*"
            else:
                word += " "
        word += "\n"
    return word


def printm():
    word = ""
    for row in range(7):
        for column in range(15):
            if (row == 0 and (column == 0 or column == 14)) or\
               (row == 1 and (column == 0 or column == 2 or column == 14 or column == 12)) or\
               (row == 2 and (column == 0 or column == 3 or column == 14 or column == 11)) or\
               (row == 3 and (column == 0 or column == 4 or column == 14 or column == 10)) or\
               (row == 4 and (column == 0 or column == 5 or column == 14 or column == 9)) or\
               (row == 5 and (column == 0 or column == 6 or column == 14 or column == 8)) or\
               (row == 6 and (column == 0 or column == 7 or column == 14)):
                word += "*"
            else:
                word += " "
        word += "\n"
    return word


def printn():
    word = ""
    for row in range(7):
        for column in range(9):
            if (row == 0 and (column == 0 or column == 8)) or\
               (row == 1 and (column == 0 or column == 2 or column == 8)) or\
               (row == 2 and (column == 0 or column == 3 or column == 8)) or\
               (row == 3 and (column == 0 or column == 4 or column == 8)) or\
               (row == 4 and (column == 0 or column == 5 or column == 8)) or\
               (row == 5 and (column == 0 or column == 6 or column == 8)) or\
               (row == 6 and (column == 0 or column == 7 or column == 8)):
                word += "*"
            else:
                word += " "
        word += "\n"
    return word


def printo():
    word = ""
    for row in range(7):
        for column in range(8):
            if (row == 0 and (column == 1 or column == 2 or column == 3 or column == 4 or column == 5 or column == 6)) or\
               (row == 1 and (column == 0 or column == 7)) or\
               (row == 2 and (column == 0 or column == 7)) or\
               (row == 3 and (column == 0 or column == 7)) or\
               (row == 4 and (column == 0 or column == 7)) or\
               (row == 5 and (column == 0 or column == 7)) or\
               (row == 6 and (column == 1 or column == 2 or column == 3 or column == 4 or column == 5 or column == 6)):
                word += "*"
            else:
                word += " "
        word += "\n"
    return word


def printp():
    word = ""
    for row in range(7):
        for column in range(6):
            if (row == 0 and (column == 0 or column == 1 or column == 2 or column == 3 or column == 4 or column == 5)) or\
               (row == 1 and (column == 0 or column == 5)) or\
               (row == 2 and (column == 0 or column == 1 or column == 2 or column == 3 or column == 4 or column == 5)) or\
               (row == 3 and (column == 0)) or\
               (row == 4 and (column == 0)) or\
               (row == 5 and (column == 0)) or\
               (row == 6 and (column == 0)):
                word += "*"
            else:
                word += " "
        word += "\n"
    return word


def printq():
    word = ""
    for row in range(7):
        for column in range(6):
            if (row == 0 and (column == 0 or column == 1 or column == 2 or column == 3 or column == 4 or column == 5)) or\
               (row == 1 and (column == 0 or column == 5)) or\
               (row == 2 and (column == 0 or column == 1 or column == 2 or column == 3 or column == 4 or column == 5)) or\
               (row == 3 and (column == 3)) or\
               (row == 4 and (column == 3)) or\
               (row == 5 and (column == 3)) or\
               (row == 6 and (column == 3 or column == 4 or column == 5)):
                word += "*"
            else:
                word += " "
        word += "\n"
    return word


def printr():
    word = ""
    for row in range(7):
        for column in range(6):
            if (row == 0 and (column == 0 or column == 1 or column == 2 or column == 3 or column == 4 or column == 5)) or\
               (row == 1 and (column == 0 or column == 5)) or\
               (row == 2 and (column == 0 or column == 1 or column == 2 or column == 3 or column == 4 or column == 5)) or\
               (row == 3 and (column == 0 or column == 2)) or\
               (row == 4 and (column == 0 or column == 3)) or\
               (row == 5 and (column == 0 or column == 4)) or\
               (row == 6 and (column == 0 or column == 5)):
                word += "*"
            else:
                word += " "
        word += "\n"
    return word


def prints():
    word = ""
    for row in range(7):
        for column in range(6):
            if (row == 0 and (column == 0 or column == 1 or column == 2 or column == 3 or column == 4 or column == 5)) or\
               (row == 1 and (column == 0)) or\
               (row == 2 and (column == 0)) or\
               (row == 3 and (column == 0 or column == 1 or column == 2 or column == 3 or column == 4 or column == 5)) or\
               (row == 4 and (column == 5)) or\
               (row == 5 and (column == 5)) or\
               (row == 6 and (column == 0 or column == 1 or column == 2 or column == 3 or column == 4 or column == 5)):
                word += "*"
            else:
                word += " "
        word += "\n"
    return word


def printt():
    word = ""
    for row in range(7):
        for column in range(7):
            if (row == 0 and (column == 0 or column == 1 or column == 2 or column == 3 or column == 4 or column == 5 or column == 6)) or\
               (row == 1 and (column == 3)) or\
               (row == 2 and (column == 3)) or\
               (row == 3 and (column == 3)) or\
               (row == 4 and (column == 3)) or\
               (row == 5 and (column == 3)) or\
               (row == 6 and (column == 3)):
                word += "*"
            else:
                word += " "
        word += "\n"
    return word


def printu():
    word = ""
    for row in range(7):
        for column in range(6):
            if (row == 0 and (column == 0 or column == 5)) or\
               (row == 1 and (column == 0 or column == 5)) or\
               (row == 2 and (column == 0 or column == 5)) or\
               (row == 3 and (column == 0 or column == 5)) or\
               (row == 4 and (column == 0 or column == 5)) or\
               (row == 5 and (column == 0 or column == 5)) or\
               (row == 6 and (column == 1 or column == 2 or column == 3 or column == 4)):
                word += "*"
            else:
                word += " "
        word += "\n"
    return word


def printv():
    word = ""
    for row in range(7):
        for column in range(13):
            if (row == 0 and (column == 0 or column == 12)) or\
               (row == 1 and (column == 1 or column == 11)) or\
               (row == 2 and (column == 2 or column == 10)) or\
               (row == 3 and (column == 3 or column == 9)) or\
               (row == 4 and (column == 4 or column == 8)) or\
               (row == 5 and (column == 5 or column == 7)) or\
               (row == 6 and (column == 6)):
                word += "*"
            else:
                word += " "
        word += "\n"
    return word


def printw():
    word = ""
    for row in range(7):
        for column in range(11):
            if (row == 0 and (column == 0 or column == 10)) or\
               (row == 1 and (column == 0 or column == 10)) or\
               (row == 2 and (column == 0 or column == 10)) or\
               (row == 3 and (column == 0 or column == 5 or column == 10)) or\
               (row == 4 and (column == 0 or column == 4 or column == 6 or column == 10)) or\
               (row == 5 and (column == 0 or column == 3 or column == 7 or column == 10)) or\
               (row == 6 and (column == 0 or column == 10)):
                word += "*"
            else:
                word += " "
        word += "\n"
    return word


def printx():
    word = ""
    for row in range(7):
        for column in range(13):
            if (row == 0 and (column == 0 or column == 12)) or\
               (row == 1 and (column == 2 or column == 10)) or\
               (row == 2 and (column == 4 or column == 8)) or\
               (row == 3 and (column == 6)) or\
               (row == 4 and (column == 4 or column == 8)) or\
               (row == 5 and (column == 2 or column == 10)) or\
               (row == 6 and (column == 0 or column == 12)):
                word += "*"
            else:
                word += " "
        word += "\n"
    return word


def printy():
    word = ""
    for row in range(7):
        for column in range(7):
            if (row == 0 and (column == 0 or column == 6)) or\
               (row == 1 and (column == 1 or column == 5)) or\
               (row == 2 and (column == 2 or column == 4)) or\
               (row == 3 and (column == 3)) or\
               (row == 4 and (column == 3)) or\
               (row == 5 and (column == 3)) or\
               (row == 6 and (column == 3)):
                word += "*"
            else:
                word += " "
        word += "\n"
    return word


def printz():
    word = ""
    for row in range(7):
        for column in range(6):
            if (row == 0 and (column == 0 or column == 1 or column == 2 or column == 3 or column == 4 or column == 5)) or\
               (row == 1 and (column == 5)) or\
               (row == 2 and (column == 4)) or\
               (row == 3 and (column == 3)) or\
               (row == 4 and (column == 2)) or\
               (row == 5 and (column == 1)) or\
               (row == 6 and (column == 0 or column == 1 or column == 2 or column == 3 or column == 4 or column == 5)):
                word += "*"
            else:
                word += " "
        word += "\n"
    return word


def user_input():
    while True:
        s = input("Enter the alphabetic word: ").strip().lower()
        if all(c.isalpha() or c.isspace() for c in s) and len(s) > 0:
            return s
        else:
            print("Enter only alphabetic letters and spaces.")


def main():
    s = user_input()
    print("👇 The letters you enters 👇\n")

    letters = {
        'a': printa, 'b': printb, 'c': printc, 'd': printd, 'e': printe,
        'f': printf, 'g': printg, 'h': printh, 'i': printi, 'j': printj,
        'k': printk, 'l': printl, 'm': printm, 'n': printn, 'o': printo,
        'p': printp, 'q': printq, 'r': printr, 's': prints, 't': printt,
        'u': printu, 'v': printv, 'w': printw, 'x': printx, 'y': printy,
        'z': printz
    }

    lines = []
    for char in s:
        if char in letters:
            lines.append(letters[char]().splitlines())
        elif char == ' ':
            space_block_width = 2
            lines.append([" " * space_block_width for i in range(7)])

    for row_idx in range(7):
        current_display_line = []
        for char_line in lines:
            current_display_line.append(char_line[row_idx])

        print(" ".join(current_display_line))


if __name__ == "__main__":
    main()
