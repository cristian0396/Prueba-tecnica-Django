from django.urls.conf import path
from django.urls.resolvers import URLPattern


from . import views
from django.urls import path

urlpatterns=[
    path('', views.ShowChatHome, name ='showChat'),
    path('room/<str:room_name>/<str:person_name>', views.ShowChatPage, name='showchat'),
]