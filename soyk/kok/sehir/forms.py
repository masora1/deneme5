from django import forms
from .models import City

class Sehirform(forms.ModelForm):
    class Meta:
        model = City
        fields = ('Mahalle', 'Ilce', 'Numara', 'Ev', 'Tarih')
