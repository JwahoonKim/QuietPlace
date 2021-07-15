from django.urls import path
import accounts.views

urlpatterns = [
    path('accounts/', accounts.views.signup, name='signup'),
    path('accounts/login/', accounts.views.login, name='login'),
    path('accounts/revise', accounts.views.revise, name='revise'),
]
