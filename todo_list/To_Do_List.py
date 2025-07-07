import json
from pathlib import Path

Filename = Path(r"D:\Project\python\todo_list\todo_listdata.json").absolute()

the_list = []
completed_list = []
categories = ['Work', 'Personal', 'Other']


def save_data():
    data = {
        "active_tasks": the_list,
        "completed_tasks": completed_list,
        "categories": categories
    }
    with open(Filename, 'w') as f:
        json.dump(data, f)


def load_data():
    global the_list, completed_list, categories
    if Filename.exists():
        with open(Filename, 'r') as f:
            data = json.load(f)
            the_list = data.get("active_tasks", [])
            completed_list = data.get("completed_tasks", [])
            categories = data.get("categories", ["Work", "Personal", "Other"])


def display_task(tasks, title="Tasks"):
    print(f"\n{title}: ")
    if not tasks:
        print("No tasks found")
    else:
        for i, task in enumerate(tasks):
            if isinstance(task, dict):
                print(f"{i}. {task['name']} [Category: {task['category']}]")
            else:
                print(f"{i}. {task}")


def add_task():
    new_task = input("Enter a new task: ").strip()
    if not new_task:
        print("Task cannot be empty!")
        return

    print("\nAvailable categories:")
    for i, category in enumerate(categories):
        print(f"{i}. {category}")
    print(f"{len(categories)}. Add new category")

    category_choice = input(
        f"Choose category (0-{len(categories)}), or press ENTER for no category: ").strip()

    if category_choice == str(len(categories)):
        new_category = input("Enter new category name: ").strip()
        if new_category:
            categories.append(new_category)
            the_list.append({"name": new_task, "category": new_category})
    elif category_choice.isdigit() and 0 <= int(category_choice) < len(categories):
        the_list.append(
            {"name": new_task, "category": categories[int(category_choice)]})
    elif not category_choice:
        the_list.append(new_task)
    else:
        print("Invalid category choice. Task added without category.")
        the_list.append(new_task)

    save_data()


def remove_task():
    display_task(the_list, "Current Tasks")
    if the_list:
        try:
            remove_task = int(
                input("Enter the number of the task to remove: "))
            if 0 <= remove_task < len(the_list):
                the_list.pop(remove_task)
                save_data()
            else:
                print("Invalid task number")
        except ValueError:
            print("Enter a valid number")


def mark_completed():
    # Fixed: was using undefined 'tasks'
    display_task(the_list, "Current Tasks")
    if the_list:
        try:
            completed_task = int(
                input("Enter the number of the completed task: "))
            if 0 <= completed_task < len(the_list):
                completed_list.append(the_list[completed_task])
                the_list.pop(completed_task)
                save_data()
            else:
                print("Invalid task number.")
        except ValueError:
            print("Enter a valid number.")


def filtered_category():
    print("\nAvailable categories:")
    for i, category in enumerate(categories):
        print(f"{i}. {category}")
    print(f"{len(categories)}. Show uncategorized tasks")

    try:
        category_number = int(input("Enter category number to filter: "))
        if 0 <= category_number < len(categories):
            selected_category = categories[category_number]
            filtered_tasks = [task for task in the_list
                              if isinstance(task, dict) and task['category'].lower() == selected_category.lower()]
            display_task(filtered_tasks, f"Tasks in '{selected_category}'")
        elif category_number == len(categories):
            uncategorized = [
                task for task in the_list if not isinstance(task, dict)]
            display_task(uncategorized, "Uncategorized Tasks")
        else:
            print("Invalid category number.")
    except ValueError:
        print("Enter a valid number.")


load_data()

while True:
    print("\nTodo List Menu:"
          "\n1. View Active Tasks"
          "\n2. View Completed Tasks"
          "\n3. Add a Task"
          "\n4. Remove a Task"
          "\n5. Mark Task as Completed"
          "\n6. Filter Tasks by Category"
          "\n7. Exit")
    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            display_task(the_list)
        elif choice == 2:
            display_task(completed_list, "Completed Tasks")
        elif choice == 3:
            add_task()
        elif choice == 4:
            remove_task()
        elif choice == 5:
            mark_completed()
        elif choice == 6:
            filtered_category()
        elif choice == 7:
            print("\nThanks for using the program!")
            break
        else:
            print("Invalid choice. Please enter a number between 1-7.")
    except ValueError:
        print("Please enter a valid number.")
