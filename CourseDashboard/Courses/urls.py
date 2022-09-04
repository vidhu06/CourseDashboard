from django.urls import path

from . import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('courseEnrollment/', views.UsersEnrollment.as_view())
]
