from django.shortcuts import render, HttpResponse

# Create your views here.
def tambah(request, num1, num2):
    context = {
        'title': 'Kalkulator Tambah',
        'num1': num1,
        'num2': num2,
        'result': f"{num1} + {num2} = {num1+num2}",
    }
    return render(request, 'kalkulator/index.html', context)

def kurang(request, num1, num2):
    context = {
        'title': 'Kalkulator Kurang',
        'num1': num1,
        'num2': num2,
        'result': f"{num1} - {num2} = {num1-num2}",
    }
    return render(request, 'kalkulator/index.html', context)

def kali(request, num1, num2):
    context = {
        'title': 'Kalkulator Kali',
        'num1': num1,
        'num2': num2,
        'result': f"{num1} x {num2} = {num1*num2}",
    }
    return render(request, 'kalkulator/index.html', context)

def bagi(request, num1, num2):
    context = {
        'title': 'Kalkulator Bagi',
        'num1': num1,
        'num2': num2,
        'result': f"{num1} / {num2} = {num1/num2}",
    }
    return render(request, 'kalkulator/index.html', context)
