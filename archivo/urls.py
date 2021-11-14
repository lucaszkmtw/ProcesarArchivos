from django.urls import path
from archivo import views

urlpatterns = [
    path('', views.index , name='home'),
]
