import re
from celery import Celery


app = Celery('tasks_celery', 
             backend='rpc://',
             broker='pyamqp://localhost//')

@app.task
def add(x, y):
    return x + y

