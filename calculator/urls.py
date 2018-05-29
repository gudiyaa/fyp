from django.conf.urls import url, include
from .views import Index,Home,About,Contact,Director,Registrar,Core,Gallery
from . import views

urlpatterns=[
    url(r'^$', Index.as_view(), name='index'),
    url(r'^home/$', Home.as_view(), name='home'),
    url(r'^about/$', About.as_view(), name='about'),
    url(r'^contact/$', Contact.as_view(), name='contact'),
    url(r'^director/$', Director.as_view(), name='director'),
    url(r'^registrar/$', Registrar.as_view(), name='registrar'),
    url(r'^director/$', Director.as_view(), name='director'),
    url(r'^registrar/$', Registrar.as_view(), name='registrar'),
    url(r'^core/$', Core.as_view(), name='core'),
    url(r'^gallery/$', Gallery.as_view(), name='gallery'),
    url(r'^personal/$', views.personaldata, name='personal'),
    url(r'^qualification/$', views.qualificationdata, name='qualification'),
    url(r'^research/$', views.researchdata, name='research'),
    url(r'^score/$', views.scoredata, name='score'),
]