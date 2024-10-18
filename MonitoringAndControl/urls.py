from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('getData',views.getData,name='getData'),
    path('displayWest',views.displayWest,name='displayWest'),
    path('videoFeed/',views.videoFeed,name = 'videoFeed'),
]