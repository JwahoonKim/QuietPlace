from django.urls import path
from django.contrib import admin
from quietPlace import views
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
import accounts.views
import quietPlace


urlpatterns = [
    path('', views.index, name='index'),
    path('cafe/', quietPlace.views.cafe, name='cafe'),
    path('recommendation', quietPlace.views.recommendation, name='recommendation'),
    path('my_page', quietPlace.views.my_page, name='my_page'),
    path('likeCafe/', quietPlace.views.likeCafe, name='likeCafe'),
    path('cafeList/', quietPlace.views.cafeList, name='cafeList'),
    path('cafe_review', quietPlace.views.cafe_review, name='cafe_review'),
    path('newcafe/', quietPlace.views.new_cafe, name='new_cafe'),
]
