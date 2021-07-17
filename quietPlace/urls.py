from django.urls import path
from django.contrib import admin
from quietPlace import views
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
import accounts.views


urlpatterns = [
    path('my_page/', views.my_page, name='my_page'),
    path('my_page/likeCafe/', views.likeCafe, name='likeCafe'),
    path('recommendation/', views.recommendation, name='recommendation'),
    path('cafeList/', views.cafeList, name='cafeList'),
    path('cafe/<int:id>/', views.show, name='cafe'),
    path('cafe/<int:id>/cafe_review/', views.Reviewview.create, name='review'),
    path('cafe/<int:id>/cafe_review/<int:cid>', views.Reviewview.delete, name='review_delete'),
    path('newcafe/', views.new_cafe, name='new_cafe'),
]
