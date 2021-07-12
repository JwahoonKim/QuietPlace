from django.urls import path
from quietPlace import views
import accounts.views
import quietPlace

# url app별로 분리하자~~

urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', accounts.views.signup, name='signup'),
    path('accounts/login/', accounts.views.login, name='login'),
    path('header/', quietPlace.views.header, name='header'),
    path('cafe/', quietPlace.views.cafe, name='cafe'),
]
