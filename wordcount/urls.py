from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name='home'),
    # what ever name is below should be in "home.html" too. ({% url 'count' %})
    path('count', views.count, name='count'),
    path('about', views.about, name='about'),
]
