**Flask Todo App**

This is a simple Flask app for managing tasks. It provides a RESTful API for creating, updating, and deleting tasks.
Requirements

This app requires Python 3.x and the following Python modules:

Flask,
sqlite3



Installation:

Clone the repository:

$ git clone https://github.com/memorisanka/ToDo_Flask

Install the required Python modules:
$ pip install -r requirements.txt

Usage:

To start the app, run the following command in the terminal:
python app.py


API Endpoints

The app provides the following API endpoints:

GET /api/tasks: Returns a list of all tasks.
GET /api/tasks/<task_id>: Returns details of a specific task.
POST /api/tasks: Creates a new task.
PUT /api/tasks: Updates an existing task.
DELETE /api/tasks/<task_id>: Deletes a specific task.