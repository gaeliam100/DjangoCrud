from django.urls import include, path
from rest_framework import routers
from task.views import TaskViewSet
router=routers.DefaultRouter()
router.register(r'task',TaskViewSet)
urlpatterns=[
    path("api/v1/",include(router.urls)),
    path("api/v1/delete_completed_tasks/",TaskViewSet.delete_completed_tasks)
]