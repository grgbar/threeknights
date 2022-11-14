from django.contrib.auth.views import LogoutView
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='google_login'),
    path('exercise/<int:exercise_id>', views.exercise_by_id, name='exercise_by_id'),
    #path('admin', views.login, name='google_login'),
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view(), name="logout"),
    
]