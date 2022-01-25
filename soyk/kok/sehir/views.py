from django.shortcuts import render,redirect
from .models import City
from .forms import Sehirform
def merhaba (request):
    liste = City.objects.all()
    return render(request, 'sehir/giris.html', {'Sehirler':liste})

def ekle (request):
    #form = Ulkeform()
    if request.method == 'POST':
        form = Sehirform(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = Sehirform()
    return render(request, 'sehir/ekle.html', {'form':form})

def sil(request,id):
    kayit = City.objects.get(id=id)
    kayit.delete()
    return redirect('/')