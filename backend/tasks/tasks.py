from celery import shared_task
from osint_tools.four_chan import get_catalog, Board
from pprint import pprint
import time
'''
Many resources on the web recommend using celery.task. 
This might cause circular imports since you'll have to import the Celery instance.
We used shared_task to make our code reusable, which, again, requires current_app in create_celery instead of creating a new Celery instance. 
Now, we can copy this file anywhere in the app and it will work as expected.
'''
@shared_task(name='tasks.sanity_task')
def sanity_task():
    # time.sleep(45)
    return 2 + 2


@shared_task(name='tasks.get_pol')
def get_pol():
    # time.sleep(45)
    data = get_catalog(Board.b)
    assert data is not None
    assert len(data) > 0
    pprint(data[:1])

