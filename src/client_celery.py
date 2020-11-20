from .tasks_celery import add


r = add.delay(3, 5)

# print(r, type(r))
print(r.ready(), r.get(timeout=1))