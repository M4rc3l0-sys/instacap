from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['quote']  # Solo permitimos ingresar la cita
        widgets = {
            'quote': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
