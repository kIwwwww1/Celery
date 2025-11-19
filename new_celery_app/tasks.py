from celery import Celery

# 'tasks' — имя приложения Celery (используется в логах, идентификаторах и структуре задач)
# broker — URL брокера сообщений (место, куда Celery складывает задачи)
# backend — URL backend-а (место, куда Celery пишет результаты задач)
app = Celery('tasks', 
            broker='redis://localhost:6379/0', 
            backend='redis://localhost:6379/1'
)

@app.task()
def add(x, y):
    return x**2 + y**2