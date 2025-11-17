from celery_app import add

def create_tast():
    return add.delay(3, 3)

