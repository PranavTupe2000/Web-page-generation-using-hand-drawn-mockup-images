from django.urls import path
from . import views

urlpatterns=[
    path('', views.MainView.as_view(), name='Main'),
	path('', views.marksView.as_view(), name='marks'),
	
]