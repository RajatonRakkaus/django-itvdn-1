from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def year_archive(request, year):
    if year == 2003:
        return HttpResponse(f'special')
    return HttpResponse(f"{year}")

# def bio(request, username):
#     return render(request, 'index.html')


