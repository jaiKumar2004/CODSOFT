class ToDoList:
    def __init__(self):
        self.tasks = []

    def create_task(self, task):
        self.tasks.append(task)
        print("Task added successfully!")

    def read_tasks(self):
        if self.tasks:
            print("Your To-Do List:")
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task}")
        else:
            print("Your To-Do List is empty.")

    def update_task(self, index, new_task):
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1] = new_task
            print("Task updated successfully!")
        else:
            print("Invalid task index.")

    def delete_task(self, index):
        if 1 <= index <= len(self.tasks):
            del self.tasks[index - 1]
            print("Task deleted successfully!")
        else:
            print("Invalid task index.")

def main():
    todo_list = ToDoList()

    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            todo_list.create_task(task)
        elif choice == '2':
            todo_list.read_tasks()
        elif choice == '3':
            index = int(input("Enter task index to update: "))
            new_task = input("Enter new task: ")
            todo_list.update_task(index, new_task)
        elif choice == '4':
            index = int(input("Enter task index to delete: "))
            todo_list.delete_task(index)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
