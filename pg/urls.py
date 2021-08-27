"""photograpy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from pg.views import home, PortfolioView, resume, blog, contact

app_name = 'pg'
urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^portfolio/$', PortfolioView.as_view(), name='portfolio'),
    url(r'^resume/$', resume, name='resume'),
    url(r'^blog/$', blog, name='blog'),
    url(r'^contact/$', contact, name='contact')
]