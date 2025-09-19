from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://tasks_user:change_me@db:5432/tasksdb')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    done = db.Column(db.Boolean, default=False)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/addTask', methods=['POST'])
def add_task():
    data = request.json or {}
    t = Task(title=data.get('title','untitled'))
    db.session.add(t); db.session.commit()
    return jsonify({"id": t.id, "title": t.title}), 201

@app.route('/deleteTask/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    t = Task.query.get(task_id)
    if not t:
        return jsonify({"error":"not found"}), 404
    db.session.delete(t); db.session.commit()
    return jsonify({"status":"deleted"}), 200

@app.route('/listTasks', methods=['GET'])
def list_tasks():
    tasks = Task.query.all()
    return jsonify([{"id":t.id,"title":t.title,"done":t.done} for t in tasks])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
