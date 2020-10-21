"""mountain URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from mainhome import views as mh
urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', mh.test, name='testpg'), # django 제대로 실행 여부 확인용
    path('maps/', mh.f_maps, name='mapspg'), # folium maps와 연결
    path('', mh.home, name='home'),
    path('mountainlist/', mh.mountainlist, name='mountainlist'),
    #path('detail/<str:lat><str:lon>', mh.detail, name='detail'),
    path('detail/<str:latlon>', mh.detail, name='detail'),

]
