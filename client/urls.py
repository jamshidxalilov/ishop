from django.urls import path
from .views import ClientIndex


app_name='client'
urlpatterns = [
    path('', ClientIndex.as_view(), name="index"),
]
