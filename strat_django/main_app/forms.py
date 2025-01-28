from django import forms
from .models import Roadmap, Ideas

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Roadmap
        fields = ['title', 'file']

class IdeaForm(forms.ModelForm):
    class Meta:
        model = Ideas
        fields = ['mindmap', 'title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the idea title',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Describe your idea',
                'rows': 5,
            }),
            'mindmap': forms.Select(attrs={
                'class': 'form-control',
            }),
        }