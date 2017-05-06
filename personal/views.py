from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render


def home(request):
    return render_to_response("personal/include/home.html")


def contact(request):
    return render(request, 'personal/include/basic.html',
                  {'content': ['Please contact me by E-mail', 'jh94798@gmail.com']})
