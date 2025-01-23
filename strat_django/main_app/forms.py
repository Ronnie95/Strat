from django import forms
from .models import Roadmap

class UploadFileForm(forms.Form):
    model = Roadmap
    fields = ['title', 'file']