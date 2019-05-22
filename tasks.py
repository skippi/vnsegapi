from invoke import task
from vnsegapi.server import make_app

@task
def dev(ctx):
    app = make_app()
    app.run()
