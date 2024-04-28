from django.urls import path

from cloudapp.views import MainListView

app_name = 'cloudapp'

urlpatterns = [
    path('', MainListView.as_view(), name='main')
]