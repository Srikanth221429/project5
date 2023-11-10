from django.shortcuts import render

# Create your views here.
def macha(request):
    return render(request,'macha.html')
def uppalbalu(request):
    return render(request,'uppalbalu.html')
def demo(request):
    return render(request,'demo.html')
def practice(request):
    return render(request,'practice.html')