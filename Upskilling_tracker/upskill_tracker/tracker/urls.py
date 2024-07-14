from django.urls import path
from .views import home, create_goal, update_progress, register, progress_success

urlpatterns = [
    path('', home, name='home'),
    path('create-goal/', create_goal, name='create_goal'),
    path('update-progress/', update_progress, name='update_progress'),
    path('register/', register, name='register'),
    path('progress-success/', progress_success, name='progress_success'),
]