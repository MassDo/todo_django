from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLogin

# Prolongement de '/tasks/'

urlpatterns = [
    path('', TaskList.as_view(), name='task-list'),
    path('create/', TaskCreate.as_view(), name='task-create' ),
    path('login/', CustomLogin.as_view(), name='task-login' ),
    path('update/<int:pk>/', TaskUpdate.as_view(), name='task-update' ),
    path('delete/<int:pk>/', TaskDelete.as_view(), name='task-delete' ),
    path('<int:pk>/', TaskDetail.as_view(), name='task-detail'),
]
