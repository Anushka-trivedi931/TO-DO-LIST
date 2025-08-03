import json
import os

TODO_FILE = "todo_list.json"

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks in your list.\n")
        return
    print("\nYour To-Do List:")
    for idx, task in enumerate(tasks, start=1):
        status = "✅" if task["done"] else "❌"
        print(f"{idx}. {task['title']} [{status}]")

def add_task(tasks):
    title = input("Enter task: ")
    tasks.append({"title": title, "done": False})
    print("Task added!")

def mark_done(tasks):
    show_tasks(tasks)
    try:
        idx = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= idx < len(tasks):
            tasks[idx]["done"] = True
            print("Task marked as done!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Enter a valid number.")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        idx = int(input("Enter task number to delete: ")) - 1
        if 0 <= idx < len(tasks):
            removed = tasks.pop(idx)
            print(f"Deleted task: {removed['title']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Enter a valid number.")

def main():
    tasks = load_tasks()

    while True:
        print("\nOptions:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option: ")
        
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved. Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
# TO-DO-LIST
