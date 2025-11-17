from celery_app import add

# Метод delay() — это самый простой способ вызвать задачу асинхронно. 
# Под капотом он использует apply_async()
def create_tast():
    return add.delay(3, 3)

# apply_async() предлагает больше гибкости, 
# позволяя указать различные параметры выполнения: время и приоритет выполнения, 
# а также колбэки и errbacks:
def new_create_tast():
    return add.apply_async((3, 3), countdown=10)
# new_add будет запланирована к выполнению через 10 секунд после вызова.



# Для выполнения асинхронных задач необходимо запускаем Celery worker:
# myproject - Имя у меня == celery_app
# celery -A celery_app worker --loglevel=info
