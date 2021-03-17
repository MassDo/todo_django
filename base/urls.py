from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate

# Prolongement de '/tasks/'

urlpatterns = [
    path('', TaskList.as_view(), name='task-list'),
    path('create/', TaskCreate.as_view(), name='task-create' ),
    path('<str:pk>/', TaskDetail.as_view(), name='task-detail'),
]
