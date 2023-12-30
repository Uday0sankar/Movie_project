from django import forms
from card.models import Movies

class movieform(forms.ModelForm):
    class Meta:
        model = Movies
        fields='__all__'
