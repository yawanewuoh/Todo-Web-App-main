from django.urls import path

from .views import (
    TaskList,CreateTask,
    UpdateTask,user_login,CustomLogoutView,
    user_registration,TaskDelete
    )

urlpatterns=[
  path('',TaskList.as_view(),name='index'),
  path('login/',user_login,name='login'),
  path('logout/',CustomLogoutView,name='logout'), 
  path('register/',user_registration,name='register'),   
  path('create-task/',CreateTask.as_view(),name='task-create'),
  path('update-task/<int:pk>/',UpdateTask.as_view(),name='task-update'),
  path('delete-task/<int:pk>/',TaskDelete.as_view(),name='task-delete'),
]