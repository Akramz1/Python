import random
import string
import os


def save_password(password, filename):
    dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(dir, filename)
    with open(file_path, 'a') as f:
        f.write(password + '\n')
    print(f"Password saved to {file_path}")


def password_generator(length, include_uppercase, include_numbers, include_special):
    if length < (include_uppercase + include_numbers + include_special):
        raise ValueError(
            'Password length is too shorted for the specified criteria.')

    password = ''

    if include_uppercase:
        password += random.choice(string.ascii_uppercase)
    if include_numbers:
        password += random.choice(string.digits)
    if include_special:
        password += random.choice(string.punctuation)

    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    for i in range(length - len(password)):
        password += random.choice(characters)

    password_list = list(password)
    random.shuffle(password_list)
    return ''.join(password_list)


def main():
    passwords_amount = int(input("Enter the amount of password you want: "))
    filename = input(
        "Enter the file name you want to the save the passwords at (filename).txt: ")
    for passwords in range(1, passwords_amount+1):
        print(f"\nPassword #{passwords}:")
        while True:
            try:
                length = int(input("Enter password length (minimum 8): "))
                include_uppercase = input(
                    "Include uppercase letters? (y/n): ").lower() == 'y'
                include_numbers = input(
                    "Include numbers? (y/n): ").lower() == 'y'
                include_special = input(
                    "Include special characters? (y/n): ").lower() == 'y'

                password = password_generator(
                    length, include_uppercase, include_numbers, include_special)
                print(f"\nGenerated Password: {password}")
                save_password(password, filename)
                break
            except ValueError as e:
                print(f"Error: {e}. Please try again.")


if __name__ == "__main__":
    main()
