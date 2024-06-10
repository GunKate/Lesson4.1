import datetime
class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_as_completed(self):
        self.completed = True
        print(f"Задача '{self.description}' завершена.")

    def __str__(self):
        return f"{self.description} ({'completed' if self.completed else 'pending'}) by {self.deadline}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        new_task = Task(description, deadline)
        self.tasks.append(new_task)
        print(f"Задача '{description}' добавлена.")

    def show_tasks(self):
        if self.tasks:
            for task in self.tasks:
                print(str(task))
        else:
            print("Список задач пуст.")

    def show_pending_tasks(self):
        pending_tasks = [str(task) for task in self.tasks if not task.completed]
        return "\n".join(pending_tasks) if pending_tasks else "No pending tasks."


task_manager = TaskManager()
task_manager.add_task("выпить кофе", "2024-04-19")
task_manager.add_task("съесть пирожок", "2024-04-19")
task_manager.add_task("откусить яблоко", "2024-04-19")
task_manager.show_tasks()
task_manager.tasks[0].mark_as_completed()
task_manager.show_tasks()
print(task_manager.show_pending_tasks())
