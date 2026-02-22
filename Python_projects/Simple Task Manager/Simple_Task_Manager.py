def show_menu():
    print("\n--- TASK MANAGER ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            print("\nYOUR TASKS:")
            if not tasks:
                print("Your list is empty.")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

        elif choice == '2':
            new_task = input("Enter the task: ")
            tasks.append(new_task)
            print("Task added!")

        elif choice == '3':
            if not tasks:
                print("Nothing to remove.")
                continue
            index = int(input("Enter task number to remove: ")) - 1
            if 0 <= index < len(tasks):
                removed = tasks.pop(index)
                print(f"Removed: {removed}")
            else:
                print("Invalid number.")

        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
