import sqlite3

def create_db():
    conn = sqlite3.connect('todo_list.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            due_date TEXT,
            priority TEXT,
            status TEXT DEFAULT 'pending'
        )
    ''')
    conn.commit()
    conn.close()

def add_task():
    description = input("Enter task description: ")
    due_date = input("Enter due date (optional): ")
    priority = input("Enter priority (low/medium/high): ")

    conn = sqlite3.connect('todo_list.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO tasks (description, due_date, priority) VALUES (?, ?, ?)
    ''', (description, due_date, priority))
    conn.commit()
    conn.close()
    print("✅ Task added!")

def view_tasks():
    conn = sqlite3.connect('todo_list.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    conn.close()

    if tasks:
        for task in tasks:
            print(f"\n📝 ID: {task[0]}\nDescription: {task[1]}\nDue: {task[2]}\nPriority: {task[3]}\nStatus: {task[4]}\n")
    else:
        print("No tasks found.")

def mark_done():
    task_id = input("Enter task ID to mark as done: ")
    conn = sqlite3.connect('todo_list.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET status = "done" WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    print("✅ Task marked as done!")

def delete_task():
    task_id = input("Enter task ID to delete: ")
    conn = sqlite3.connect('todo_list.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    print("🗑️ Task deleted.")

def menu():
    while True:
        print("\n===== To-Do List Menu =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_done()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    create_db()
    menu()
