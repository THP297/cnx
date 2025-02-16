from django.urls import path
from .views import (
    index,
    component_accordion,
)

app_name = 'phoenix-example'

urlpatterns = [
    path('index/', index, name='index'),
    path('index/components/accordion', component_accordion, name='component-accordion'),
]
