from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('', views.PostList.as_view()),
    path('<int:pk>/', csrf_exempt(views.PostDetail.as_view())),
    path('seeOthers/', views.seeOthers,name='seeOthers'),
]
