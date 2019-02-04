from django.http import HttpResponse

def index(request):
    return HttpResponse("this is my firs page ffs")

def about(request):
    return HttpResponse("Haldaaaaaaaaaaaaaaaaalo")

def contacts(request):
    return HttpResponse("Daddaaaaaaaaaaaaadadadadaa")

def portfolio(request):
    return HttpResponse("nedadadadadadadnen")
