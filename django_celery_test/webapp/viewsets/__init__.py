from rest_framework import viewsets
from rest_framework.response import Response
from celery.result import AsyncResult

from webapp.tasks import xsum


class AsyncTaskTestViewset(viewsets.ModelViewSet):

    def create(self, request, *args, **kwargs):
        print(args)
        print(kwargs)

        print(request.data)
        numlist = request.data

        res = xsum.delay(numlist)
        # print(res)

        data = {'task': str(res)}
        return Response(data)
    

class CeleryTaskResultViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        # Retrieve task result using Celery's AsyncResult
        task_result = AsyncResult(pk)
        
        # Check if task is ready (completed)
        if task_result.ready():
            # Get the result if available
            result = task_result.result
            return Response({'result': result})
        else:
            # Task is still pending or in-progress
            return Response({'status': 'pending'})