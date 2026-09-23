from django import forms
from .models import Pokemon

class PokemonForm(forms.ModelForm):
    Nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ej: Pikachu'}))
    Tipo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ej: Eléctrico'}))
    Descripcion = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','placeholder': 'Ej: Un Pokémon de tipo eléctrico muy popular.'}))
    Imagen = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}))




    class Meta:
        model = Pokemon
        fields = '__all__'