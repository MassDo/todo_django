from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLogin, RegisterPage

from django.contrib.auth.views import LogoutView

# Prolongement de '/tasks/'

urlpatterns = [
    path('login/', CustomLogin.as_view(), name='task-login' ),
    path('logout/', LogoutView.as_view(next_page='task-login'), name='task-logout' ),
    path('register/', RegisterPage.as_view(), name='task-register' ),

    path('', TaskList.as_view(), name='task-list'),
    path('create/', TaskCreate.as_view(), name='task-create' ),
    path('update/<int:pk>/', TaskUpdate.as_view(), name='task-update' ),
    path('delete/<int:pk>/', TaskDelete.as_view(), name='task-delete' ),
    path('<int:pk>/', TaskDetail.as_view(), name='task-detail'),
]
