from django.urls import path, re_path, include
from . import views as user_views

urlpatterns = [
    # path('statistiche/', include('statistiche.urls')),
    # path('login/', include('login.urls')),
    re_path(r'^$', user_views.one_page, name = "profilo"),
    re_path(r'^paginaLavoro/$', user_views.paginaLavoro, name = "lavoro"),
    re_path(r'^paginaAltro/$', user_views.paginaAltro, name = "altro"),
]