class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def mark_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
        else:
            print("Invalid task index.")

    def display_tasks(self):
        for idx, task in enumerate(self.tasks):
            status = "Done" if task["completed"] else "Not Done"
            print(f"{idx + 1}. {task['task']} - {status}")

def main():
    todo_list = ToDoList()

    while True:
        print("\n1. Add Task")
        print("2. Mark Task as Completed")
        print("3. Display Tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
            print("Task added!")

        elif choice == "2":
            todo_list.display_tasks()
            index = int(input("Enter the task index to mark as completed: ")) - 1
            todo_list.mark_completed(index)
            print("Task marked as completed!")

        elif choice == "3":
            todo_list.display_tasks()

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
