'''
The To-Do app will have the following features:

Add a task.
View all tasks.
Mark a task as complete.
Delete a task.
Exit the app.
'''
tasks=[]
task_id=1
def add_task():
    global task_id
    task_name=input("Enter the task name: ")
    tasks.append({"id":task_id,"name":task_name,"status":False})
    task_id+=1
    
def view_tasks():
    if not tasks:
        print("No tasks available")
    print("\nYour tasks")
    for task in tasks:
        status="Completed" if task["status"] else "Pending"
        print(f"{task['id']}. {task['name']} - {status}")
    print()


def mark_complete():
    try:
        task_id=int(input("Enter the task id to mark as complete: "))
        for task in tasks:
            if task["id"]==task_id:
                if task["status"]:
                    print("Task is already completed")
                else:
                    task["status"]=True
                    print(f"Task {task_id} marked as completed")
                return
        print("Task not Found.")
    except ValueError:
        print("Invalid task id. Please enter a number.")


def delete_task():
    try:
        task_id=int(input("Enter the task id to delete: "))
        for task in tasks:
            if task["id"]==task_id:
                tasks.remove(task)
                print(f"Task {task_id} deleted")
                return
        print("Task not found.")
    except ValueError:
        print("Invalid task id. Please enter a valid Task Id.")

def main():
    while True:
        print("\nTo-Do App Menu")
        print("1. Add a task")
        print("2. View all tasks")
        print("3. Mark a task as complete")
        print("4. Delete a task")
        print("5. Exit the app")
        choice=input("Choose an option(1-5): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_complete()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting the To-Do app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__=="__main__":
    main()