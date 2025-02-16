from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    return render(request, "home/index.html")


def manage_telesales_campaign(request: HttpRequest) -> HttpResponse:
    context = {
        'active': 'manage_telesales_campaign'
    }
    return render(request, "home/manage_telesales/campaign.html", context)
