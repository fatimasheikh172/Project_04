todo_list = []


def show_menu():
    print("\n📋 To-Do List Menu:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")


while True:
    show_menu()
    choice = input("Choose the option (1 - 4): ")

    if choice == "1":
        if not todo_list:
             print("📝 Your to-do list is empty.")
        else:
            print("📝 Your Tasks:")
            for i, task in enumerate(todo_list, 1):
                print(f"{i}. {task}")

    elif choice == "2":
        task = input("Enter the task to add: ")
        todo_list.append(task)
        print(f"✅ '{task}' added to your list.")

    elif choice == "3":
        task_num = int(input("Enter the task number to remove: "))
        if 0 < task_num <= len(todo_list):
            removed = todo_list.pop(task_num - 1)
            print(f"❌ Removed '{removed}' from the list.")
        else:
            print("⚠️ Invalid task number.")
    elif choice == "4":
        print("👋 Exiting To-Do List App. Goodbye!")
        break

    else:
        print("⚠️ Invalid choice. Please enter 1 to 4.")
