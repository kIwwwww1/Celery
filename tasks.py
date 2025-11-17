# from celery import Celery

# celery_app = Celery('myapp', broker='redis://localhost:6379/0')

# @celery_app.task(rate_li)
# def add(x, y):
#     return x + y

from celery import Celery

celery_app = Celery('myapp', broker='redis://localhost:6379/0')

@celery_app.task(rate_limit='10/m')
def add(x, y):
    return x + y
