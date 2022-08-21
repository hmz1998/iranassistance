from django.urls import re_path

from . import views as pages_views

app_name = 'pages'

urlpatterns = [
    re_path(
        '^register/$',
        pages_views.Register.as_view(),
        name='register'
    ),
    
        re_path(
        '^login/$',
        pages_views.Login.as_view(),
        name='login'
    ),
]