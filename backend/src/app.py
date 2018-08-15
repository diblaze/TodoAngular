# coding=utf-8

from flask import Flask, jsonify, request, abort
from flask_cors import CORS

from .entities.entity import Session, engine, Base
from .entities.todo import Todo, TodoSchema

# creating the Flask application
app = Flask(__name__)
CORS(app)

# if needed, regenerate database schema
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


# TODO: Move this to own file
class InvalidInputException(Exception):
    def __init__(self, message, status_code=400):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code
        self.payload = dict(success=False)

    def to_dict(self):
        result = self.payload
        result["message"] = self.message
        return result


@app.errorhandler(500)
def internal_error(error):
    return "500 Error"


@app.errorhandler(InvalidInputException)
def handle_invalid_input(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.route("/todos")
def get_todos():
    # fetching from the database
    session = Session()
    todo_objects = session.query(Todo).all()

    # transforming into JSON-serializable objects
    schema = TodoSchema(many=True)
    todos = schema.dump(todo_objects)

    # serializing as JSON
    session.close()
    return jsonify(todos.data)


@app.route("/todos", methods=["POST"])
def add_todo():
    # convert post object to TodoSchema
    todo_post = TodoSchema(only=["title"]).load(request.get_json())

    if not todo_post.data:
        raise InvalidInputException("Todo needs a title")

    todo = Todo(**todo_post.data)

    # add todo to db
    session = Session()
    session.add(todo)
    session.commit()

    # return created todo
    new_todo = TodoSchema().dump(todo).data
    session.close()
    return jsonify(new_todo), 201
