from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/',views.register_user,name="register"),
    path('edit_profile/', views.edit_profile,name="edit"),
    path('change_password/',views.change_password,name="change_password"),
    path('workout/',views.workout,name="workout"),
    path('programs/',views.programs,name="programs"),
    path('health_living/',views.health_living,name="health_living"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
]
