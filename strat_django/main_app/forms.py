from django import forms
from .models import Roadmap

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Roadmap
        fields = ['title', 'file']

