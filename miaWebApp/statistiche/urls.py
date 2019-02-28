# from django.contrib import admin
# from django.urls import path, re_path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('statistiche/', include('statistiche.urls')),
# ]

from django.urls import path, include, re_path
from . import views
from django.views.generic import ListView, DeleteView

urlpatterns = [
    re_path(r'^$', views.one_page, name="Page"),
]

#inserire altro end point /function