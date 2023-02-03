tasks = []

def add_task(task):
    tasks.append(task)
    print("Task Added:", task)

def view_tasks():
    print("Tasks:")
    for i, task in enumerate(tasks):
        print(i + 1, task)

def complete_task(index):
    try:
        task = tasks.pop(index - 1)
        print("Task Completed:", task)
    except IndexError:
        print("Invalid Task Index")

while True:
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        task = input("Enter Task: ")
        add_task(task)
    elif choice == 2:
        view_tasks()
    elif choice == 3:
        index = int(input("Enter Task Index: "))
        complete_task(index)
    elif choice == 4:
        break
    else:
        print("Invalid Choice")
