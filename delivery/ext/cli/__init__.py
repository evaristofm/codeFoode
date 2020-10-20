import click
from delivery.ext.db import db
from delivery.ext.auth.models import User
from delivery.ext.db import models #noqa, o migrate precisa saber os models do app



def init_app(app):
    @app.cli.command()
    def create_db():
        """ Criando o DB """
        db.create_all()

    @app.cli.command()
    @click.option("--email", "-e")
    @click.option("--passwd", "-p")
    @click.option("--admin", "-a", is_flag=True, default=False)
    def add_user(email, passwd, admin):
        """ Adicionando novo user """
        user = User(
            email=email,
            passwd=passwd,
            admin=admin
        )
        db.session.add(user)
        db.session.commit()

        click.echo(f"Usuário {email} criado com sucesso!")

    