from new_celery_app.tasks import add, fragile_task

# res = add.delay(2, 3)
# print('task id:', res.id)
# print('ready?', res.ready())
# print('result:', res.get(timeout=10))
