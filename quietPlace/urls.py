from django.urls import path
from quietPlace import views

urlpatterns = [
    path('', views.index, name='index'), # 'localhost:8000/posts/'
]