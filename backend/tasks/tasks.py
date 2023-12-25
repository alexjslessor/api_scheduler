# import celery
# from celery.signals import after_setup_logger
# from celery import shared_task
# from celery.utils.log import get_task_logger

# from ..deps import get_rss, get_pol as get_pol_dep
# from ..settings import get_settings
# # from ..init import logger
# import asyncio

# import logging


# settings = get_settings()
# # https://docs.celeryq.dev/en/stable/userguide/tasks.html#logging
# logger = get_task_logger(__name__)
# # logger = logging.getLogger(__name__)

# # @celery.signals.after_setup_logger.connect
# # def on_after_setup_logger(**kwargs):
# #     logger = logging.getLogger('celery')
# #     logger.propagate = True
# #     logger = logging.getLogger('celery.app.trace')
# #     logger.propagate = True

# # @after_setup_logger.connect()
# # def on_after_setup_logger(logger, **kwargs):
# #     file_handler = logging.FileHandler('celery.log')
# #     formatter = logger.handlers[0].formatter
# #     file_handler.setFormatter(formatter)
# #     logger.addHandler(file_handler)
    
# # https://docs.celeryq.dev/en/stable/userguide/signals.html#std-signal-setup_logging
# # @celery.signals.setup_logging.connect
# # def on_setup_logging(**kwargs):
#     # pass

# # root = logging.getLogger()

# # if self.app.conf.worker_hijack_root_logger:
# #     root.handlers = []
# #     get_logger('celery').handlers = []
# #     get_logger('celery.task').handlers = []
# #     get_logger('celery.redirected').handlers = []

# # # Configure root logger
# # self._configure_logger(
# #     root, logfile, loglevel, format, colorize, **kwargs
# # )

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
#         logger.info(f'tasks.get_pol start')
#         # is_complete = await get_pol_dep()
#         is_complete = asyncio.run(get_pol_dep())
#         logger.info(f'tasks.get_pol  end')
#         return True
#     except Exception as e:
#         logger.error(e)
#         raise

# @shared_task(name='tasks.get_rss_celery')
# def get_rss_celery():
#     try:
#         logger.info(f'tasks.get_rss start')
#         # is_complete = await get_rss()
#         is_complete = asyncio.run(get_rss())
#         logger.info(f'tasks.get_rss  end: {is_complete}')
#         return True
#     except Exception as e:
#         logger.error(e)
#         raise
