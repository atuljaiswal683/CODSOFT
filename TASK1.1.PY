

tasks = {}

def add_task():
    task_id = len(tasks) + 1
    task_name = input("Enter task description: ")
    tasks[task_id] = task_name
    print("Task added successfully.")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for key, value in tasks.items():
            print(f"{key}. {value}")

def update_task():
    task_id = int(input("Enter task number to update: "))
    if task_id in tasks:
        tasks[task_id] = input("Enter new task description: ")
        print("Task updated.")
    else:
        print("Task not found.")

def delete_task():
    task_id = int(input("Enter task number to delete: "))
    if task_id in tasks:
        del tasks[task_id]
        print("Task deleted.")
    else:
        print("Task not found.")

while True:
    print("\n1.Add  2.View  3.Update  4.Delete  5.Exit")
    choice = input("Choose option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        break
    else:
        print("Invalid choice.")
