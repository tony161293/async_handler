from django.http import HttpResponse
#from django.shortcuts import render_to_response
import simplejson as json

from celery.result import AsyncResult
from tasks import long_task


def start_celery_task(request):
    task = long_task.delay()
    if(task):
        task = AsyncResult(task.id)
        data = task.result or task.state
        return HttpResponse(json.dumps(data), content_type= 'applicatoin/json')
    else:
        task = long_task.delay()


    #return render_to_response('start.html', {
                        #'task_id': task.id})
    #return HttpResponseRedirect("%s%s" % ('/celery_porgress?task_id=', task.id))

##def monitor_celery_ask(request):
    #if 'task_id' in request.GET:
        #task_id = request.GET['task_id']
    #else:
        #return HttpResponse('No task id passed')

    #task = AsyncResult(task_id)
    #data = task.result or task.state
    #return render_to_response('work.html',
            #{'data': data})
    ##return HttpResponse(data)