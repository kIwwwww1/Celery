from celery import Celery
from celery.utils.log import get_task_logger

# 'tasks' — имя приложения Celery (используется в логах, идентификаторах и структуре задач)
# broker — URL брокера сообщений (место, куда Celery складывает задачи)
# backend — URL backend-а (место, куда Celery пишет результаты задач)
app = Celery('tasks', 
            broker='redis://localhost:6379/0', 
            backend='redis://localhost:6379/1'
)

logger = get_task_logger(__name__)

@app.task()
def add(x, y):
    return x**2 + y**2

@app.task(bind=True, max_retries=3)
def fragile_task(self, x):
    try:
        if x == 0:
            raise ValueError('bad value')
        return 10 / x
    except Exception as e:
        logger.warning('Ошибка, пробуем повторить: %s', e)
        raise self.retry(exc=e, countdown=10)