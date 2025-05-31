task_list = []

def display_menu():
    print("Welcome to the Task Manager!")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as completed")
    print("4. Remove a task")
    print("5. Exit")

def add_task():
    task = input("Enter the task description: ")
    if task != "":
        task_list.append({"description": task, "completed": False})
        print(f"Task '{task}' added.\n")
    else:
        print("Task cannot be empty. Please try again.")
        return
    
def view_tasks():
    if not task_list: 
        print("No tasks available.\n")
    else:
        print("\n--- Current Tasks ---") 
        for index, task in enumerate(task_list):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{index + 1}. {task['description']} - {status}")
        print("--------------------\n")


def mark_task_as_completed():
    view_tasks()
    if task_list:
        try:
            task_index = int(input("Enter the task number to mark as completed: ")) - 1
            if 0 <= task_index < len(task_list):
                task_list[task_index]["completed"] = True
                print(f"Task '{task_list[task_index]['description']}' marked as completed.\n")
            else:
                print("Invalid task number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def remove_task():
    view_tasks()
    if task_list:
        try:
            task_index = int(input("Enter the task number to remove: ")) - 1
            if 0 <= task_index < len(task_list):
                removed_task = task_list.pop(task_index)
                print(f"Task '{removed_task['description']}' removed.")
            else:
                print("Invalid task number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        print("--------------------")
        
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_task_as_completed()
        elif choice == '4':
            remove_task()
        elif choice == '5':
            print("Exiting the Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again and enter a number between 1 & 5.")

if __name__ == "__main__": 
    main()
