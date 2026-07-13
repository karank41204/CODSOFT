class Task:
    def __init__(self,  title ):
        self.title = title
        self.completed =  False

    def mark_completed(self):
        self.completed =  True

    def __str__(self):
        status = "✔" if  self.completed else "✘"
        return f"[{status}] {self.title}"


class ToDoList:
    def __init__(self):
        self.tasks = [ ]

    def add_task(self, title):
        self.tasks.append(Task(title))
        print("Task  added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("\nNo tasks  available.")
            return

        print("\n------ TO-DO LIST -----")
        for i, task in enumerate(self.tasks,start=1):
            print(f"{i}. {task}")

    def complete_task(self, index):
        if 0 <= index < len(self.tasks ):
            self.tasks[index].mark_completed()
            print("Task marked as completed!")
        else:
            print("Invalid  task number.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")


def main():
    todo = ToDoList()

    while True:
        print("\n====== TO-DO LIST MENU ======")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1 ":
            title = input("Enter task:  ")
            todo.add_task(title)

        elif  choice == "2":
            todo.view_tasks()

        elif choice == "3":
            todo.view_tasks( )
            try:
                task_no = int(input("Enter task number: "))
                todo.complete_task(task_no  - 1)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            todo.view_tasks()
            try:
                task_no = int(input("Enter task number  to delete: "))
                todo.delete_task(task_no - 1)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "5":
            print("Thank you for  using the To-Do List App!")
            break

        else:
            print("Invalid choice ! Try again.")


if __name__ == "__main__":
    main()