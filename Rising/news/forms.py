from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'announs', 'text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'placeholder': 'Title',
                'class': 'form-control'
            }),
            'announs': TextInput(attrs={
                'placeholder': 'Announsments',
                'class': 'form-control'
            }),
            'text': Textarea(attrs={
                'placeholder': 'Text of Announsments',
                'class': 'form-control'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Date of publication'
            })
        }