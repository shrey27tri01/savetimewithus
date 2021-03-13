from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('edit/',views.edit,name='editaccount'),
    path('signup/',views.SignUpView.as_view(),name='signup'),
]