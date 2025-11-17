from celery import Celery, Some

celery_app = Celery('myapp', broker='redis://localhost:6379/0')

# ограничивает скорость выполнения задач.
#  Например, если нужно, чтобы задача add выполнялась чаще, чем 10 раз в минуту, можно настроить rate_limit
@celery_app.task(rate_limit='10/m')
def add(x, y):
    return x + y


# Задача может иногда терпеть неудачу из-за проблем (которые вечно бывают):
# Задача попытается выполниться до 3 раз с интервалом в 60 секунд, если возникнет временная ошибка
@celery_app.task(bind=True, max_retries=3, default_retry_delay=60)
def new_add(self, x, y):
    try:
        return x + y
    except Exception as e:
        raise self.retry(e=e)

