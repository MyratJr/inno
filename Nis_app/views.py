# nis_app/views.py
from django.shortcuts import render, redirect
from .models import Country, InnovationPractice, Message
from django.http import HttpResponse


def index(request):
    return redirect("/tk")


def home(request, lg):
    countries = Country.objects.all()
    return render(request, 'home.html', {'countries': countries, "LANGUAGE_CODE":lg})

def country_detail(request, pk, lg):
    country = Country.objects.get(pk=pk)
    practices = InnovationPractice.objects.filter(country=country)
    print(practices.count())
    return render(request, 'country_detail.html', {'country': country, 'practices': practices, "LANGUAGE_CODE":lg})


def about_theme(request, lg):
    return render(request, 'detail.html', {"LANGUAGE_CODE":lg})


def message(request, lg):
    if request.method == 'POST':
        title = request.POST.get('title')
        fullname = request.POST.get('fullname')
        desc = request.POST.get('desc')
        email = request.POST.get('gmail')
        contact = Message(title=title, fullname=fullname, desc=desc, gmail=email)
        contact.save()
        countries = Country.objects.all()
        return render(request, "home.html", {"success":"success", 'countries': countries, "LANGUAGE_CODE":lg})

    return render(request, 'contact.html', {"LANGUAGE_CODE":lg})




def success_view(request):
    return HttpResponse("Thank you for contacting us. We will get back to you soon.")