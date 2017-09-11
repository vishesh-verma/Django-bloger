
from django.conf.urls import url,include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from blog import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blogss/', views.blogsList.as_view()),
    url(r'^blog/',include('blog.urls')),
]

urlpatterns= format_suffix_patterns(urlpatterns)
