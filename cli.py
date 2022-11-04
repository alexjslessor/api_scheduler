import typer
from invoke import run

set_env = 'source ./env && test_env'
app = typer.Typer()

@app.command()
def terra_deploy():
    cmd = f'{set_env} && cd tf && ./deploy'
    result = run(cmd, hide=False, warn=True)
    if result.ok:
        print(result.stdout)

@app.command()
def startup():
    cmd = f'{set_env} && uvicorn main:app --reload --port $PORT'
    result = run(cmd, hide=False, warn=True)
    if result.ok:
        print(result.stdout)

@app.command()
def install_pkg():
    cmd = f'{set_env} && pip install $LIBRARY_LOCAL --force-reinstall'
    result = run(cmd, hide=False, warn=True)
    if result.ok:
        print(result.stdout)


# @app.command()
# def build():
#     cmd = 'rm -rf dist && poetry build'
#     result = run(cmd, hide=False, warn=True)
#     if result.ok:
#         rprint(result.stdout)

# @app.command()
# def build_publish():
#     cmd = 'rm -rf dist && poetry publish --build'
#     result = run(cmd, hide=False, warn=True)
#     if result.ok:
#         rprint(result.stdout)

# @app.command()
# def build_install():
#     cmd = 'rm -rf dist && poetry build && pip install dist/*.whl --force-reinstall'
#     result = run(cmd, hide=False, warn=True)
#     if result.ok:
#         rprint(result.stdout)

# @app.command()
# def terra_test_e2e():
#     cmd = f'{set_env} && py.test -s tests/v2/test_e2e.py'
#     result = run(cmd, hide=False, warn=True)
#     if result.ok:
#         rprint(result.stdout)

# @app.command()
# def terra_output():
#     cmd = 'cd terraform-mod && terraform output'
#     result = run(cmd, hide=True, warn=True)
#     if result.ok:
#         rprint(result.stdout)

# @app.command()
# def re_install_pkg():
#     cmd = f'{set_env} && pip install $FASTAPI_TOOLS --force-reinstall'
#     result = run(cmd, hide=False, warn=True)
#     if result.ok:
#         rprint(result.stdout)


if __name__ == "__main__":
    app()

