from django.urls import path
from quietPlace import views
import accounts.views
import quietPlace

# url app별로 분리하자~~

urlpatterns = [
    path('', views.index, name='index'),
    path('header/', quietPlace.views.header, name='header'),
    path('cafe/', quietPlace.views.cafe, name='cafe'),
    path('recommendation', quietPlace.views.recommendation, name='recommendation'),
    path('my_page', quietPlace.views.my_page, name='my_page'),
    path('likeCafe/', quietPlace.views.likeCafe, name='likeCafe'),
    path('cafeList/', quietPlace.views.cafeList, name='cafeList'),
    path('cafe_review', quietPlace.views.cafe_review, name='cafe_review'),
    path('newcafe/', quietPlace.views.new_cafe, name='new_cafe'),
]
