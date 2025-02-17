from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    return render(request, "home/index.html")

def customer_info_form(request: HttpRequest) -> HttpResponse:
    context = {
        "active_tab": "customer-info",
    }
    return render(request, "home/components/forms/customer-info-form.html", context)

def contact_info_form(request: HttpRequest) -> HttpResponse:
    context = {
        "active_tab": "contact-info",
    }
    return render(request, "home/components/forms/contact-info-form.html", context)

def address_info_form(request: HttpRequest) -> HttpResponse:
    context = {
        "active_tab": "address-info",
    }
    return render(request, "home/components/forms/address-info-form.html", context)

def payment_info_form(request: HttpRequest) -> HttpResponse:
    context = {
        "active_tab": "payment-info",
    }
    return render(request, "home/components/forms/payment-info-form.html", context)

def product_info_form(request: HttpRequest) -> HttpResponse:
    context = {
        "active_tab": "product-info",
    }
    return render(request, "home/components/forms/product-info-form.html", context)

def phone_info_form(request: HttpRequest) -> HttpResponse:
    context = {
        "active_tab": "phone-info",
    }
    return render(request, "home/components/forms/phone-info-form.html", context)

def manage_telesales_campaign(request: HttpRequest) -> HttpResponse:
    tabs = [
        {"id": "customer-info", "label": "Customer Info", "url": "home:customer-info-form"},
        {"id": "contact-info", "label": "Contact Info", "url": "home:contact-info-form"},
        {"id": "payment-info", "label": "Payment Info", "url": "home:payment-info-form"},
        {"id": "product-info", "label": "Product Info", "url": "home:product-info-form"},
        {"id": "address-info", "label": "Address Info", "url": "home:address-info-form"},
        {"id": "phone-info", "label": "Phone Info", "url": "home:phone-info-form"},
    ]
    context = {
        'active': 'manage_telesales_campaign',
        'tabs': tabs,
    }
    return render(request, "home/manage_telesales/campaign.html", context)
