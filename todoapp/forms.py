from django import forms
from .models import Post

class AddForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text',)
        widgets = { 'text':forms.TextInput(attrs={'class':'form-control' ,
        'placeholder':'Enter a task to do'}),
        }
