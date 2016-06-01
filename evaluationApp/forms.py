from django import forms
from .models import evaluation201606

class evaluation201606Form(forms.ModelForm):
    
    class Meta:
        model = evaluation201606
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(attrs={'size': 40}),
            }
