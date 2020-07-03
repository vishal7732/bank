from django.shortcuts import render
from .models import bankinfo

def home(request):
    return render(request, 'home.html')

def name(request):
    return render(request, 'ho.html')

def get_info(request):
    if request.method == "POST":
        g_ifsc = request.POST["g_ifsc1"]
        a=int(g_ifsc)
        info = bankinfo.objects.all()    
        detail={'detail':info, 'g_ifsc':a}
    return render(request, 'home.html', detail)

def get_info_city(request):
    if request.method == "POST":
        g_ifsc = request.POST["g_ifsc"]
        city = request.POST["city"]
        
        info = bankinfo.objects.all()    
        detail={'detail':info, 'g_ifsc':g_ifsc, 'city':city}
    return render(request, 'ho.html', detail)

