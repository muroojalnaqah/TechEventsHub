from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('login', views.login, name = "login"),
    path('register', views.register, name = "register"),
    path('contactus', views.contactus, name = "contactus"),
    path('user', views.user, name = "user"),
    path('aboutus', views.aboutus, name = "aboutus"),
    path('courses', views.courses, name = "courses"),
    path('events', views.events, name = "events"),
    path('useredit', views.useredit, name = "useredit"),

]