from django.urls import path
from . import views
from .views import nuevo_post_view

urlpatterns = [
    path('', views.posts ),
    path('nuevo/', nuevo_post_view, name='nuevo_post'),

]
