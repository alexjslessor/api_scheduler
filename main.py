from backend.entry import create_app

app = create_app()
# celery = app.celery_app

# def auto_reload_celery_worker():
#     from watchgod import run_process
#     import subprocess

#     def run_worker():
#         subprocess.call(
#             ["celery", "-A", "main.celery", "worker", "--loglevel=info"]
#         )

#     run_process("./backend", run_worker)


if __name__ == "__main__":
    app
    # auto_reload_celery_worker()