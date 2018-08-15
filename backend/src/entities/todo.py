from sqlalchemy import Column, String, Boolean
from marshmallow import Schema, fields

from .entity import Entity, Base


class Todo(Entity, Base):
    __tablename__ = "todos"

    title = Column(String, nullable=False)
    completed = Column(Boolean, default=False)
    marked_as_removed = Column(Boolean, default=False)

    def __init__(self, title):
        Entity.__init__(self)
        self.title = title
        self.completed = False


class TodoSchema(Schema):
    id = fields.Number()
    title = fields.Str()
    completed = fields.Boolean()
    marked_as_removed = fields.Boolean()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()
