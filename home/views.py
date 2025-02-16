from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    return render(request, "home/index.html")

def customer_info_form(request: HttpRequest) -> HttpResponse:
    context = {
        "active_tab": "customer-info",
    }
    return render(request, "home/components/customer-info-form.html", context)

def contact_info_form(request: HttpRequest) -> HttpResponse:
    context = {
        "active_tab": "contact-info",
    }
    return render(request, "home/components/contact-info-form.html", context)

def address_info_form(request: HttpRequest) -> HttpResponse:
    context = {
        "active_tab": "address-info",
    }
    return render(request, "home/components/address-info-form.html", context)

def payment_info_form(request: HttpRequest) -> HttpResponse:
    context = {
        "active_tab": "payment-info",
    }
    return render(request, "home/components/payment-info-form.html", context)

def product_info_form(request: HttpRequest) -> HttpResponse:
    context = {
        "active_tab": "product-info",
    }
    return render(request, "home/components/product-info-form.html", context)

def phone_info_form(request: HttpRequest) -> HttpResponse:
    context = {
        "active_tab": "phone-info",
    }
    return render(request, "home/components/phone-info-form.html", context)

def manage_telesales_campaign(request: HttpRequest) -> HttpResponse:
    context = {
        'active': 'manage_telesales_campaign'
    }
    return render(request, "home/manage_telesales/campaign.html", context)
