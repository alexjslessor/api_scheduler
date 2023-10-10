# from celery import shared_task
# from osint_tools.four_chan import get_catalog, Board
# from ..settings import get_settings
# from celery.utils.log import get_task_logger

# settings = get_settings()
# # https://docs.celeryq.dev/en/stable/userguide/tasks.html#logging
# logger = get_task_logger(settings.TASK_LOGGER)
# '''
# Many resources on the web recommend using celery.task. 
# This might cause circular imports since you'll have to import the Celery instance.
# We used shared_task to make our code reusable, which, again, requires current_app in create_celery instead of creating a new Celery instance. 
# Now, we can copy this file anywhere in the app and it will work as expected.
# '''
# @shared_task(name='tasks.sanity_task')
# def sanity_task():
#     logger.info(f'sanity_task success')
#     return 2 + 2


# @shared_task(name='tasks.get_pol')
# def get_pol():
#     try:
#         logger.info(f'pol success')
#         data = get_catalog(Board.pol)
#         # assert data is not None
#         # assert len(data) > 0
#         logger.info(data[:1])
#         return True
#     except Exception as e:
#         logger.error(e)
#         raise



