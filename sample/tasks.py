from models import CounterModel
from celery.task import task
from celery import current_task
from time import sleep

@task()
def add_two_numbers(a, b):
    sleep(10)
    count = CounterModel.objects.create(count=a + b)
    return count

@task()
def long_task():
    while(1):
        a=1
        a=a+1
        sleep(0.2)
        current_task.update_state(state= "PROGRESS", meta=
                {'current': a,'total': 100})
