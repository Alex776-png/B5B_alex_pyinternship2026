tasks = []

def add_task(task):
    tasks.append(task)

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
    else:
        print("Task not found:", task)

def show_tasks():
    print("Current tasks:")
    for task in tasks:
        print("-", task)


# Add 5 tasks
add_task("Complete Python assignment")
add_task("Study list comprehensions")
add_task("Practice loops")
add_task("Read a Python chapter")
add_task("Submit assignment")

# Display tasks
show_tasks()

# Remove 2 tasks
remove_task("Practice loops")
remove_task("Read a Python chapter")

# Display remaining tasks
print("\nAfter removing 2 tasks:")
show_tasks()