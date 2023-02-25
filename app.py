import sqlite3

from flask import Flask, request

app = Flask(__name__)


def connect_to_db():
    conn = sqlite3.connect('todo.db')
    return conn


def create_db_table():
    conn = connect_to_db()
    try:
        conn.execute('''CREATE TABLE tasks (
        id INTEGER PRIMARY KEY, 
        task TEXT);''')
        conn.commit()
        print('Tasks table created successfully.')
    except sqlite3.OperationalError:
        print('There is a problem with creating Tasks table!')
    finally:
        conn.close()


def add_task(task):
    task_to_add = {}
    conn = connect_to_db()
    try:
        cur = conn.cursor()
        cur.execute("INSERT INTO tasks (task) VALUES (?) RETURNING id", (task["task"],))
        new_task_id = cur.fetchone()[0]
        conn.commit()
        task_to_add = get_task_by_id(new_task_id)

    except sqlite3.OperationalError:
        conn.rollback()

    finally:
        conn.close()

    return task_to_add


def get_task_by_id(task_id):
    task = {}
    conn = connect_to_db()
    try:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute('SELECT * FROM tasks WHERE id= ?', (task_id,))
        row = cur.fetchone()

        task["id"] = row["id"]
        task["task"] = row["task"]

    except sqlite3.OperationalError:
        task = {}

    return task


def get_tasks():
    tasks = []
    conn = connect_to_db()
    try:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM tasks")
        rows = cur.fetchall()

        for row in rows:
            task = {"id": row["id"], "task": row["task"]}

            tasks.append(task)

    except sqlite3.OperationalError:
        tasks = []

    return tasks


def update_task(task):
    updated_task = {}
    conn = connect_to_db()
    try:
        cur = conn.cursor()
        cur.execute("UPDATE tasks SET task = ? WHERE id =?",
                    (task["task"], task["id"],))
        conn.commit()

        updated_task = get_task_by_id(task["id"])

    except sqlite3.OperationalError:
        conn.rollback()
        updated_task = {}
    finally:
        conn.close()

    return updated_task


def delete_task(task_id):
    message = {}
    try:
        conn = connect_to_db()
        conn.execute("DELETE from tasks WHERE id = ?",
                     (task_id,))
        conn.commit()
        message["status"] = "Task deleted successfully"
    except sqlite3.OperationalError:
        conn.rollback()
        message["status"] = "Cannot delete task"
    finally:
        conn.close()

    return message


@app.route('/api/tasks', methods=['GET'])
def api_get_tasks():
    return get_tasks()


@app.route('/api/tasks/<task_id>', methods=['GET'])
def api_get_task(task_id):
    return get_task_by_id(task_id)


@app.route('/api/tasks', methods=['POST'])
def api_add_task():
    task = request.get_json()
    return add_task(task)


@app.route('/api/tasks', methods=['PUT'])
def api_update_task():
    task = request.get_json()
    return update_task(task)


@app.route('/api/tasks/<task_id>', methods=['DELETE'])
def api_delete_user(task_id):
    return delete_task(task_id)


if __name__ == '__main__':
    create_db_table()
    app.run(debug=True)
