from django.urls import path
from .views import (
    index,
    manage_telesales_campaign,
)

app_name = 'home'

urlpatterns= [
    path('index/', index, name='index'),
    path('manage-telesales/campaign/', manage_telesales_campaign, name='manage-telesales-campaign'),
]