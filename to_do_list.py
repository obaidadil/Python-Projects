tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added:", task)

def view_tasks():
    print("Tasks:")
    for task in tasks:
        print(task)

def complete_task(task):
    tasks.remove(task)
    print("Task completed:", task)

while True:
    command = input("Enter a command (add, view, complete, quit): ")
    if command == "add":
        task = input("Enter a task: ")
        add_task(task)
    elif command == "view":
        view_tasks()
    elif command == "complete":
        task = input("Enter a task to complete: ")
        complete_task(task)
    elif command == "quit":
        break
    else:
        print("Invalid command")
