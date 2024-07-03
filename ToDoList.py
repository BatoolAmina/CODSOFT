tasks = []

# Add a new task
def add_task(task):
    tasks.append({'task': task, 'completed': False})
    print(f"Task '{task}' added.")

# View all tasks
def view_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, 1):
            status = "Done" if task['completed'] else "Not Done"
            print(f"{i}. {task['task']} - {status}")

# Update an existing task
def update_task(task_number, new_task):
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]['task'] = new_task
        print(f"Task {task_number} updated to '{new_task}'.")
    else:
        print("Invalid task number.")

# Delete a task
def delete_task(task_number):
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task['task']}' deleted.")
    else:
        print("Invalid task number.")

# Mark a task as completed
def complete_task(task_number):
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]['completed'] = True
        print(f"Task {task_number} marked as completed.")
    else:
        print("Invalid task number.")

# Main program loop
def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Done")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            task_number = int(input("Enter task number to update: "))
            new_task = input("Enter the new task: ")
            update_task(task_number, new_task)
        elif choice == '4':
            task_number = int(input("Enter task number to delete: "))
            delete_task(task_number)
        elif choice == '5':
            task_number = int(input("Enter task number to mark as completed: "))
            complete_task(task_number)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

main()
