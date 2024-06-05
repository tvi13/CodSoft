class Task:
    def __init__(self,title,description):
        self.title=title
        self.descriiption=description
        self.completed=False

    def mark_completed(self):
        self.completed=True
    
    def __str__(self):
        status="Completed" if self.completed else "Not completed"
        return f"{self.title} - {self.description} [{status}]"

class ToDoList:
    def __init__(self):
        self.tasks=[]

    def add_task(self,task):
        self.tasks.append(task)

    def update_task(self,index ,title=None,description=None):
        if 0<=index<len(self.tasks):
            if title:
                self.tasks[index].title=title
            if description:
                self.tasks[index].description=description

    def complete_task(self,index):
        if 0<=index<len(self.tasks):
            self.tasks[index].mark_completed()

    def delete_task(self,index):
        if 0<=index<len(self.tasks):
            self.tasks.pop(index)
    
    def list_tasks(self):
        return self.tasks

from streamlit import *

if 'todo_list' not in session_state:
    session_state.todo_list = ToDoList()

def add_task():
    title=text_input("Task Title",key=title)
    description=text_area("Task Description",key="description")
    if button("Add Task"):
        task=Task(title,description)
        session_state.todo_list.add_task(task)
        success("Task added successfully.")
        experimental_rerun()

def update_task(index):
    title=text_input("New Task Title",value=todo_list.tasks[index].title,key=f"title_{index}")
    descrription=text_area("New Task Description",value=session_state.todo_list.tasks[index].description,key=f"description_{index}")
    if button("Update Task",key=f"update_{index}"):
        session_state.todo_list.update_task(index,title,description)
        success("Task updated successfully.")
        experimental_rerun()

def complete_task(index):
    if button("Completed Task",key=f"complete_{index}"):
        session_state.todo_list.complete_task(index)
        success("Task marked as completed.")
        experimental_rerun

def delete_task(index):
    if button("Delete Task",key=f"delete_{index}"):
        session_state.todo_list.delete_task(index)
        success("Task deleted successfully.")
        experimental_rerun

def main():
    title("To-Do List Application")
    header("Add new task")
    add_task()
    header("Your list")
    tasks=session_state.todo_list.list_tasks()
    for i,tasks in enumerate(tasks):
        subheader(f"Task {i+1}")
        write(task)
        update_task(i)
        complete_task(i)
        delete_task(i)

if __name__=="__main__":
    main()