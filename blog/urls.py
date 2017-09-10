from django.conf.urls import url
from . import views

app_name="blog"


urlpatterns=[

url(r'^$', views.index, name="index"),

url(r'^add/$' , views.add, name="add"),
url(r'^view/$' , views.view, name="view"),
url(r'^showadd/$' , views.showadd, name="showadd"),
url(r'^show/$' , views.show, name="show"),
url(r'^signup/$' , views.signup, name="signup"),
url(r'^signupaf/$' , views.signupaf, name="signupaf"),
url(r'^delete/$' , views.delete, name="delete"),


]
