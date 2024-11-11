from django import forms
from .models import Art  # Assurez-vous d'importer le modèle Art si vous l'utilisez
class UpdateArt(forms.ModelForm):
    class Meta:
        model = Art  # Remplacez par le nom de votre modèle Art
        fields = ['title', 'category', 'price', 'tags', 'description']
class AddArt(forms.ModelForm):
    class Meta:
        model = Art  
        fields = ['title', 'category', 'price', 'tags', 'description','file']    
