def add_task(tasks):
    """Prompts the user to enter a task description and append it to our `tasks` list."""
    task = input("Enter a task to add: ")
    tasks.append(task)
    print("Task successfully added!")


def view_tasks(tasks):
    """Iterate over the `tasks` list and display each task."""
    if tasks:
        print("*" * 50)
        print("Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")
        print("*" * 50)
    else:
        print("*" * 50)
        print("You currently have no tasks.")
        print("*" * 50)


def remove_task(tasks):
    """Allow the user to specify the index of the task they want to remove. We also handle the case
    where the user enters an invalid index."""
    view_tasks(tasks)
    if tasks:
        try:
            index = int(input("Enter the task number to remove: ")) - 1
            if 0 <= index < len(tasks):
                del tasks[index]
                print("Task successfully removed.")
            else:
                print("You have entered an invalid task number.")
        except ValueError:
            print("Please enter a valid task number.")


def save_tasks(tasks):
    """Writes the list of tasks to a file, with each task on a new line."""
    with open('../../IdeaProjects/PythonProjects/tasks.txt', 'w') as file:
        for task in tasks:
            file.write(task + '\n')
    print("Tasks successfully saved.")


def load_tasks():
    """Read the tasks from a file and add them back into our tasks list."""
    tasks = []
    try:
        with open('../../IdeaProjects/PythonProjects/tasks.txt', 'r') as file:
            tasks = [line.strip() for line in file]
        print("Tasks successfully loaded.")
    except FileNotFoundError:
        print("There are no saved tasks found.")
    return tasks


def main_menu():
    """Function to set up the main menu that allows the user to choose an action."""
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Tasks")
    print("4. Save Tasks")
    print("5. Load Tasks")
    print("6. Exit")
    choice = input("Enter your choice: ")
    return choice


def main():
    # Load tasks at the start of the app
    tasks = load_tasks()
    while True:
        choice = main_menu()
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            save_tasks(tasks)
        elif choice == '5':
            load_tasks()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1-6.")


main()
