from django.shortcuts import render
import django.contrib.staticfiles

# Create your views here.
def showHome(request):
    return render(request, 'Index.html')
