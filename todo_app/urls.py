
from django.urls import path
from todo_app import views


urlpatterns = [
    path('',views.index,name='index'),
    path('delete/<int:task_id>/',views.delete,name='delete'),
    path('update/<int:id>',views.update,name='update')
]