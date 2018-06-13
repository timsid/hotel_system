from django.http import HttpResponse

def HelloWorld(request):
    return HttpResponse('Hello Django')

def WelcomePage(request):
    return HttpResponse('Welcome Page')