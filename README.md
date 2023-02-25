***Flask Todo App***<br>
<br>
This is a simple Flask app for managing tasks. It provides a RESTful API for creating, updating, and deleting tasks.
<br><br>
**Requirements:**<br>
<br>
This app requires Python 3.x and the following Python modules:<br>

Flask,
sqlite3
<br>
<br>

**Installation:**<br>
<br>
Clone the repository:<br>

$ git clone https://github.com/memorisanka/ToDo_Flask <br>
<br>
Install the required Python modules:<br>
$ pip install -r requirements.txt
<br><br>
**Usage:**<br>
<br>
To start the app, run the following command in the terminal:<br>
python app.py
<br>
<br>
**API Endpoints**<br>
<br>
The app provides the following API endpoints:<br>
<br>
GET /api/tasks: Returns a list of all tasks.<br>
GET /api/tasks/<task_id>: Returns details of a specific task.<br>
POST /api/tasks: Creates a new task.<br>
PUT /api/tasks: Updates an existing task.<br>
DELETE /api/tasks/<task_id>: Deletes a specific task.