from django.urls import path
from . import views

urlpatterns=[
    path('index/',views.hello),
    path('about/',views.about)
]