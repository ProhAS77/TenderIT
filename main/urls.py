from django.urls import path
from . import views
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, RegisterPage #new
from django.contrib.auth.views import LogoutView #обращение будет напрямую без представления
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='info'),
    path('create/', TaskCreate.as_view(), name='create'),
    path('task/', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('update/<int:pk>/', TaskUpdate.as_view(), name='update'),

    path('update_complete/<int:task_id>/', views.update, name='update_complete'),
    path('download/', views.download_file, name='download'),

    path('diagram/', views.generate_charts, name='diagram'),

    path('delete/<int:pk>/', TaskDelete.as_view(), name='delete'),
    path('search/', views.search, name='search'),
    path('upload_file/', views.upload_file, name='upload_file'),
    path('about/', views.about, name='about'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
