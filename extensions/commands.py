import click
from extensions.database import db
from model.medium_model import MediumModel

def create_db():
    """Creates database"""
    db.create_all()


def drop_db():
    """Cleans database"""
    db.drop_all()


def create_model_table():
    """ Create table Model in the database """
    MediumModel.__table__.create(db.engine)


def init_app(app):
    # add multiple commands in a bulk
    for command in [create_db,
                    drop_db,
                    create_model_table]:
        app.cli.add_command(app.cli.command()(command))
