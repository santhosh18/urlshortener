'''
Urls for shortener app urlshortener/urls.py
'''

from django.urls import path
from urlshortapp import views

appname = "shortener"

urlpatterns = [
    # Home view
    path("", views.home_view, name="home"),
    path('<str:shortened_part>', views.redirect_url_view, name='redirect'),
]
