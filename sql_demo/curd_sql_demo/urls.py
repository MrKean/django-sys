from django.urls import path
from . import views

# app_name = 'curd_sql_demo'

urlpatterns = [
    path('', views.person_list, name='person_list'), #主界面，所以地址为空字符


    path('create/', views.person_create, name='person_create'),
    path('update/<int:pk>/', views.person_update, name='person_update'),
    path('delete/<int:pk>/', views.person_delete, name='person_delete'),

]
