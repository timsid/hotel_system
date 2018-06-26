from django.http import HttpResponse
from django.shortcuts import render

def  DefaultView(request):

    return render(request, 'welcome.html',
        {
            'page_class': 'index',
            'page_title': 'Welcome to hotel system'
        })