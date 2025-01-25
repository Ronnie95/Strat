from django import forms
from .models import Roadmap

class UploadFileForm(forms.ModelForm):
    model = Roadmap
    fields = ['title', 'file']