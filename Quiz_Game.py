import json


def load_quiz_data(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_questions_by_category(data, category, difficulty):
    return [q for q in data if q['category'].lower() == category.lower() and q['difficulty'].lower() == difficulty.lower()]


def main():
    file_name = 'questions.json'

    quiz_data = load_quiz_data(file_name)

    choose_category = input("Enter category (Math, Science, History): ")

    choose_difficulty = input(
        "Enter the difficulty of the questions (Easy, Medium, Hard): "
    )

    questions = get_questions_by_category(
        quiz_data, choose_category, choose_difficulty
    )

    right_answers = 0

    for i, q in enumerate(questions, start=1):
        print(f"Q{i}: {q['question']}")
        for idx, option in enumerate(q['options'], start=1):
            print(f" {idx}. {option}")

        while True:
            user_answer = input("Enter the option number of your answer: ")
            if user_answer.isdigit():
                user_answer = int(user_answer)
                if 1 <= user_answer <= len(q['options']):
                    selected_option = q['options'][user_answer - 1]
                    if selected_option == q['answer']:
                        print("Correct!\n")
                        right_answers += 1
                    else:
                        print(f"Wrong! The correct answer is: {q['answer']}\n")
                    break
                else:
                    print("Invalid option, enter a valid option number.")
            else:
                print("Please enter a valid number.")

    print(f"Quiz is complete! You scored {right_answers}/10.")


main()
