from django.urls import path
from quietPlace import views
import quietPlace


urlpatterns = [
    path('', views.index, name='index'),
    path('recommendation/', quietPlace.views.recommendation, name='recommendation'),
    path('my_page/', quietPlace.views.my_page, name='my_page'),
    path('my_page/likeCafe/', quietPlace.views.likeCafe, name='likeCafe'),
    path('cafeList/', quietPlace.views.cafeList, name='cafeList'),
    path('newcafe/', quietPlace.views.new_cafe, name='new_cafe'),
    path('cafe/<int:id>/', quietPlace.views.show, name='cafe'),
    path('cafe/<int:id>/cafe_review/', quietPlace.views.Reviewview.create, name='cafe_review'),
    path('cafe/<int:id>/cafe_review/<int:cid>/', quietPlace.views.Reviewview.delete, name='review_delete'),
]
