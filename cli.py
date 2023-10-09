import typer
from invoke import run

set_env = 'source ./env && dev_env_sched'
app = typer.Typer()

@app.command()
def build_api():
    cmd = f'''
    {set_env}
    # build_local_install_pkg $LIBRARY_LOCAL
    pip install $LIBRARY_LOCAL --force-reinstall
    '''
    result = run(cmd, hide=False, warn=True)
    if result.ok:
        print(result.stdout)

@app.command()
def wipe_env():
    cmd = f'''
    {set_env}
    sver
    pip freeze | cut -d "@" -f1 | xargs pip uninstall -y
    wipeenv
    '''
    result = run(cmd, hide=False, warn=True)
    if result.ok:
        print(result.stdout)


@app.command()
def terra_deploy():
    cmd = f'{set_env} && cd tf && ./deploy'
    result = run(cmd, hide=False, warn=True)
    if result.ok:
        print(result.shell)

@app.command()
def startup():
    cmd = f'{set_env} && uvicorn main:app --reload --port $PORT'
    result = run(cmd, hide=False, warn=True)
    if result.ok:
        print(result.stdout)




if __name__ == "__main__":
    app()

