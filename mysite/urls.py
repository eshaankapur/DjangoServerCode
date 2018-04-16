"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
#from django.conf.urls import patterns, url , include
from myapp import views


#added
admin.autodiscover()

#added
"""
urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'myapp.views.index')
)
)
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),	# added ???
    path('rlist/', views.getRestaurantList),
    path('<str:restaurant>/rtype', views.getRestaurantType),
    path('<str:restaurant>/<str:date>/<str:time>/checkreservation',views.checkReservation),
    path('<str:restaurant>/<str:date>/<str:time>/bookreservation',views.bookReservation),
    path('<str:username>/<str:password>/authentication', views.authentication),
    path('<str:restaurant>/getmenu', views.getmenu),
    path('<str:username>/checkusername', views.checkusername),
    #url(r'^admin/', include(admin.site.urls)),
]
