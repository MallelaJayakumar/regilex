from django.urls import path, include
from rest_framework import routers
from .views import TaskViewSet

router = routers.DefaultRouter()
router.register('task', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

api_urlpatterns = (
    url(r'^task$', views.get_tasks,name='get_tasks'),
     url(r'^task/(<id>)$', views.get_task_by_id,name='get_task_by_id'),
     url(r'^edittask/(<id>)$', views.edit_task,name='edit_task'),
     url(r'^deletetask/(<id>)$', views.delete_task,name='delete_task'),
     url(r'^create_task$', views.create_task,name='create_task'),
     )