from django.shortcuts import render, HttpResponse

# Create your views here.
def index (request):
    return render(request, 'mywebsite/index.html')

def about (request):
    return HttpResponse("<h1 style='color:blue'>Selamat Datang di halaman about</h1>")