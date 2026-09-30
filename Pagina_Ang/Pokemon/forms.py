from django import forms
from .models import Pokemon




class PokemonForm(forms.ModelForm):
    Nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ej: Pikachu'}))
    Tipo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ej: Eléctrico'}),
    required=False)
    Descripcion = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','placeholder': 'Ej: Un Pokémon de tipo eléctrico muy popular.'}))
    Imagen = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}))




    class Meta:
        model = Pokemon
        fields = '__all__'


    def clean_Nombre(self):
        Nombre = self.cleaned_data.get('Nombre')

        if Nombre and not Nombre.isalpha() and ' ' not in Nombre:
            raise forms.ValidationError('El nombre del Pokémon solo puede contener letras y espacios.')

        return Nombre


    def clean_Descripcion(self):
        Descripcion = self.cleaned_data.get('Descripcion')

        if Descripcion and not Descripcion.isalpha() and ' ' not in Descripcion:
            raise forms.ValidationError('La descripción debe contener al menos una palabra y no puede estar vacía.')

        return Descripcion

