from flask import render_template, Blueprint, request

from todo_app.db import db
from todo_app.models.forms import TodoForm, RemoveForm
from todo_app.models.todo_item import Todo_item

view = Blueprint('view', __name__)

@view.route('/index', methods=["GET", "POST"])
@view.route('/', methods=["GET", "POST"])
def index():
    tasks = Todo_item.query.order_by(Todo_item.id).all()

    return render_template('index.html', tasks=tasks)

@view.route('/add', methods=["GET","POST"])
def add():
    add = TodoForm()
    
    if add.validate_on_submit():
        task = add.task.data
        content = Todo_item(content=task)
        # print(task, content)
        db.session.add(content)
        db.session.commit()

    tasks = Todo_item.query.order_by(Todo_item.id).all()

    return render_template('add.html', form=add, tasks=tasks)

@view.route('/remove', methods=["GET", "POST"])
def remove():

    error = None

    rem = RemoveForm()
    if rem.validate_on_submit():
        value = rem.task.data
        print('c ',value)
        try:
            task = Todo_item.query.filter_by(content=value).first()
            print(task, 'THIS IS TASK')
            db.session.delete(task)
            db.session.commit()
        except:
            error = "Task doesn't exists."
        

    tasks = Todo_item.query.order_by(Todo_item.id).all()
    
    return render_template('remove.html',  form=rem, tasks=tasks, error=error)