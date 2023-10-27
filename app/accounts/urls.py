from django.urls import path
from . import views


app_name="accounts"
urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('register/', views.RegisterView.as_view(), name="register"),
]