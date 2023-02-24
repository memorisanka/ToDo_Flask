import sqlite3

from flask import Flask, jsonify, request

app = Flask(__name__)


def connect_to_db():
    conn = sqlite3.connect('todo.db')
    return conn


def create_db_table():
    try:
        conn = connect_to_db()
        conn.execute('''CREATE TABLE tasks (
        id int PRIMARY KEY NOT NULL,
        task text NOT NULL);''')
        conn.commit()
        print('Tasks table created successfully.')
    except:
        print('There is a problem with creating Tasks table!')
    finally:
        conn.close()


def add_task(task):
    task_to_add = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO tasks (task) VALUES (?)", (task['task'],))
        conn.commit()
        task_to_add = get_task_by_id(cur.lastrowid)

    except:
        conn.rollback()

    finally:
        conn.close()

    return task_to_add


def get_task_by_id(task_id):
    task = {}
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute('SELECT * FROM tasks WHERE id= ?', (task_id,))
        row = cur.fetchone()

        task["id"] = row["id"]
        task["task"] = row["task"]

    except:
        task = {}

    return jsonify(task)


def get_tasks():
    tasks = []
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM tasks")
        rows = cur.fetchall()

        for row in rows:
            task = {"id": row["id"], "task": row["task"]}

            tasks.append(task)

    except:
        tasks = []

    return tasks


def update_task(task):
    updated_task = {}
    try:
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("UPDATE tasks SET task = ? WHERE id =?",
                    (task["task"], task["id"],))
        conn.commit()

        updated_task = get_task_by_id(task["id"])

    except:
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
    except:
        conn.rollback()
        message["status"] = "Cannot delete task"
    finally:
        conn.close()

    return message


@app.route('/api/tasks', methods=['GET'])
def api_get_tasks():
    return jsonify(get_tasks())


@app.route('/api/tasks/<task_id>', methods=['GET'])
def api_get_task(task_id):
    return jsonify(get_task_by_id(task_id))


@app.route('/api/tasks/add', methods=['POST'])
def api_add_task():
    task = request.get_json()
    return jsonify(add_task(task))


@app.route('/api/tasks/update', methods=['PUT'])
def api_update_task():
    task = request.get_json()
    return jsonify(update_task(task))


@app.route('/api/tasks/delete/<task_id>', methods=['DELETE'])
def api_delete_user(task_id):
    return jsonify(delete_task(task_id))


if __name__ == '__main__':
    app.run(debug=True)
