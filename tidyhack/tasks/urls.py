from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.homeView,name='home'),
    path('about/',views.aboutView,name='about'),
    path('list/',views.taskListView,name='tasklist'),
    path('task/new/',views.createNewTask,name='newtask'),
    path('task/update/<str:pk>/',views.updateTask,name='updatetask'),
    path('task/delete/<str:pk>/',views.deleteTask,name='deletetask'),
    path('task/complete/<str:pk>',views.completeTask,name='completetask'),
    path('scrapbook/enterDate/',views.scrapbookFormView,name='scrapbookdate'),
    path('scrapbook/<int:year>/<int:month>/<int:day>/',views.scrapbookView,name='scrapbook'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)