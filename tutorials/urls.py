from django.conf.urls import url
from tutorials import views

urlpatterns = [
    url(r'^api/tutorials$', views.tutorial_list),
]
