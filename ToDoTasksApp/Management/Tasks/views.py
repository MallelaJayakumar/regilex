from rest_framework import viewsets
from .Serializers import TaskSerializer
from .models import Task

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.Objects.all()
    serializer_class = TaskSerializer



@never_cache
@login_required(login_url='/login')
@require_GET
def get_tasks(request):
    logger.debug('Getting all tasks from database')
    # Prepare django query to retrieve all records from db using models.py
    tasks = Tasks.objects.get(s_default_task=True)
    return JsonResponse(list(tasks), status=200)


@never_cache
@login_required(login_url='/login')
@require_GET
def get_tasks(request):
    logger.debug('Getting required task from database')
    task_id = request.GET['id']
    # Prepare django query to retrieve all records from db using models.py
    tasks = Tasks.objects.filter(user_id=task_id).all()
    return JsonResponse(list(tasks), status=200)