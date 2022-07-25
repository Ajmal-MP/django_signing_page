from django.conf import settings
from django.urls import path
from .views import *
urlpatterns = [
    path('', login_page, name='login'),
    path('home/', home, name='home'),
    path('logout/', logout_page, name='logout'),
]
