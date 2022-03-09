# from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.home,name='Index'),
    # path('',views.service,name='Services'),
    path('services',views.service,name='Services'),
    path('about',views.about,name='About'),
    path('contact',views.contact,name='contact'),
    path('components',views.component,name='Component'),
    path('project',views.project,name='project'),
]