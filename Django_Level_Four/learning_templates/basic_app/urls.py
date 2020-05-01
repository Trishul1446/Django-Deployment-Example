from django.urls import path
from basic_app import views
#from django.conf.urls import url

#TEMPLATE TAGGING
app_name = "basic_app_url"

urlpatterns = [
    path('index/', views.index, name='index'),
    path('other/', views.other, name='other'),
    path('relative/', views.relative, name='relative'),
]
