import os


def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()


def write_file(filename, content, mode='w'):
    with open(filename, mode) as file:
        return file.write(content + ('\n' if mode == 'a' else ''))


def append_to_file(filename, content):
    write_file(filename, content, mode='a')


def get_user_input():
    print("\n Enter your text (type SAVE on a new line to save and exit): ")

    lines = []
    while True:
        line = input()
        if line == 'SAVE':
            break
        lines.append(line)

    return '\n'.join(lines)


def search_and_replace(content):
    print("\nCurrent content: ")
    print(content)

    word = input("\nEnter the word to replace: ")
    if word in content:
        new_word = input(f"Replace {word} with: ")
        updated_content = content.replace(word, new_word)
        print(f"Replaced {word} with {updated_content}")
        return updated_content
    else:
        print(f"{word} is not found in the file")
        return content


def main():
    # read file path if you have it in a directory
    direc = os.path.dirname(os.path.abspath(__file__))
    Filename = input("Enter file name to open or create: ")
    Filepath = os.path.join(direc, Filename)
    try:
        if os.path.exists(Filepath):
            content = read_file(Filepath)
            print("Current file content:")
            print(content)
            print("\nOptions")
            print("1. Edit (Overwrite)")
            print("2. Append")
            print("3. Search & replace")
            choice = input("Choose [1/2/3]: ").strip()
            if choice == '1':
                new_content = get_user_input()
                write_file(Filepath, new_content)
            elif choice == '2':
                new_content = get_user_input()
                append_to_file(Filepath, new_content)
            elif choice == '3':
                print(
                    "\nWhen you replace the word you change every word thats the same as the one you wrote"
                )
                updated_content = search_and_replace(content)
                write_file(Filepath, updated_content)
            else:
                pront("Invalid choice. No changes will be made")
        else:
            content = get_user_input()
            write_file(Filepath, content)

        print(f"{Filename} saved in {direc}")
    except OSError:
        print(f"Error: {Filename} could not be opened.")


if __name__ == '__main__':
    main()
