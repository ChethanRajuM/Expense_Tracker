from django.urls import path
from tracker.views import indexView

urlpatterns = [
    path('',indexView),
]