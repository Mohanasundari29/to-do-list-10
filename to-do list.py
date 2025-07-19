def display_menu():
    print("\n=== TO-DO LIST MENU ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def add_task(tasks):
    title = input("Enter task title: ")
    task = {"title": title, "completed": False}
    tasks.append(task)
    print("Task added successfully!")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["completed"] else "❌"
        print(f"{i}. {task['title']} [{status}]")

def mark_task_completed(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to mark as completed: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["completed"] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"Task '{removed['title']}' deleted.")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
