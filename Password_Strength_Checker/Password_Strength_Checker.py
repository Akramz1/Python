def Checker(password):
    has_digit = False
    has_capital_letter = False
    has_special_symbol = False
    has_alphabetic_letter = False
    has_long_length = len(password) >= 5
    missing = []

    for char in password:
        if char.isdigit():
            has_digit = True
        elif char.isalpha():
            has_alphabetic_letter = True
            if char.isupper():
                has_capital_letter = True
        elif char in '!@#$%^&*()_':
            has_special_symbol = True

    if not has_digit:
        missing.append("digits")
    if not has_capital_letter:
        missing.append("uppercase letters")
    if not has_alphabetic_letter:
        missing.append("letters")
    if not has_special_symbol:
        missing.append("special characters")
    if not has_long_length:
        missing.append("minimum length (5+ characters)")

    if has_long_length and len(password) >= 10 and has_digit and has_capital_letter and has_special_symbol and has_alphabetic_letter:
        return "Very Strong"
    elif has_long_length and has_digit and has_capital_letter and has_special_symbol and has_alphabetic_letter:
        return "Strong"
    elif has_long_length and (has_digit + has_capital_letter + has_special_symbol + has_alphabetic_letter) >= 3:
        feedback = "Medium - missing: " + \
            ", ".join(missing) if missing else "Medium"
        return feedback
    elif has_long_length:
        feedback = "Weak - missing: " + \
            ", ".join(missing) if missing else "Weak"
        return feedback
    else:
        return "Very Weak - missing: " + ", ".join(missing)


def main():
    password = input("Enter a password: ")
    print(Checker(password))


if __name__ == "__main__":
    main()
