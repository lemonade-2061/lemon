from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)
todos = []

@app.route('/') 
def index():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    if task:
        todos.append(task)
    print(todos)
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>', methods=['GET'])
def delete(task_id):
    if 0 <= task_id < len(todos):
        todos.pop(task_id)
    return redirect(url_for('index'))