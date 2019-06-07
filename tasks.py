from invoke import task
from vnsegapi.server import make_app


@task
def dev(ctx):
    app = make_app()
    app.run()


@task
def format(ctx):
    ctx.run("poetry run black .")


@task
def docker_dev(ctx):
    ctx.run("docker build -t foo .")
    ctx.run("docker run --rm -it foo")
