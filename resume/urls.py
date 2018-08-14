from django.conf.urls import url, include
from resume import views

urlpatterns = [
    url(r'^$', views.landing, name='landing'),
]
