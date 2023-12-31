#define URL route for index() view
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('menu', views.MenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token)
]