from django.urls import path
from quietPlace import views
import accounts.views

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', accounts.views.signup, name='signup' ),
]