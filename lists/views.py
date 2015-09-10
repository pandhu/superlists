from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    return HttpResponse('<html><title>To-Do</title><body>Pandhu Hutomo Aditya 1206277426</body></html>')