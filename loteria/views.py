
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render


def index(request):
    return HttpResponse("Bienvenido a nuestra pagina test")


#def index(request):
 #   return render_to_response('personal/include/home.html')
