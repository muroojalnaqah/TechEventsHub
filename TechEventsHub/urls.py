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
    path('logout', views.logout, name = "logout"),
    path('update', views.update, name = "update"),
    path('courses_search_result', views.courses_search_result, name = "courses_search_result"),
    path('events_search_result', views.events_search_result, name = "events_search_result"),


]