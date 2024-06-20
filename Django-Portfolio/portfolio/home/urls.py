from django.contrib import admin
from django.urls import path, include
from home import views
urlpatterns = [

    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('projects',views.project,name='project'),
    path('service',views.service,name='service'),

]
