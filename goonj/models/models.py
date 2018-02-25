from peewee import *


class Tag(Model):
    name = CharField(max_length=100)
    _id = IntegerField(default=1)


class SmartAlert(Model):
    created_at = DateTimeField()
    source = CharField(max_length=100)
    error_id = CharField(max_length=50)
    message = TextField(null=True)
    tags = IntegerField(default=1)
    severity = CharField(max_length=30)
    tags = ForeignKeyField(Tag)
